"""
2026-02-15-kosdaq-ipo-vc-cases.md 포스팅용 주가 차트 생성 스크립트
주가 추이(파란선) + VC 누적 순매도(빨간 step line + 핑크 fill) 이중축 차트
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from datetime import timedelta
import numpy as np
import json
import os

# ── 한글 폰트 설정 ──
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# ── 파일 경로 ──
PRICE_CSV = r'C:\Users\Peter\Desktop\코스닥신규상장분석\docs\price_trade\data\all_stocks.csv'
VC_JSON = r'C:\Users\Peter\Desktop\코스닥신규상장분석\krx_data\vc_analysis\vc_analysis_amt.json'
IPO_CSV = r'C:\Users\Peter\Desktop\코스닥신규상장분석\docs\price_trade\data\ipo_analysis.csv'
OUTPUT_DIR = r'c:\Users\Peter\github\beaten-by-the-market.github.io\assets\images\2026-02-15-kosdaq-ipo-vc-cases'

# ── 종목 설정 ──
STOCKS = {
    '475830': {
        'name': '오름테라퓨틱',
        'period': '6m',
        'title': '오름테라퓨틱 — 주가 추이와 VC 누적 순매도 (상장~6개월)',
    },
    '388210': {
        'name': '씨엠티엑스',
        'period': 'all',
        'title': '씨엠티엑스 — 주가 추이와 VC 누적 순매도 (상장 이후 전체)',
    },
    '348150': {
        'name': '고바이오랩',
        'period': '6m',
        'title': '고바이오랩 — 주가 추이와 VC 누적 순매도 (상장~6개월)',
    },
    '476830': {
        'name': '알지노믹스',
        'period': 'all',
        'title': '알지노믹스 (476830) — 주가 vs VC 누적 순매도',
    },
    '469610': {
        'name': '이노테크',
        'period': 'all',
        'title': '이노테크 — 주가 추이와 VC 누적 순매도 (상장 이후 전체)',
    },
}

# ── 데이터 로드 ──
print("Loading IPO data...")
ipo_df = pd.read_csv(IPO_CSV)
ipo_df['code_num'] = ipo_df['코드'].astype(str).str.replace('A', '', regex=False)

print("Loading price data...")
price_df = pd.read_csv(PRICE_CSV)
target_codes = ['A' + c for c in STOCKS.keys()]
price_df = price_df[price_df['코드'].isin(target_codes)].copy()
price_df['날짜'] = pd.to_datetime(price_df['날짜'])
price_df['code_num'] = price_df['코드'].str.replace('A', '', regex=False)
print(f"  → {len(price_df)} price rows loaded")

print("Loading VC data (from pre-processed JSON)...")
with open(VC_JSON, 'r', encoding='utf-8') as f:
    vc_json = json.load(f)

# early_sell_top30의 disclosures를 종목별로 정리
vc_disclosures = {}  # {stock_code: DataFrame(date, amount)}
for item in vc_json['early_sell_top30']:
    sc = str(item['stock_code'])
    if sc in STOCKS:
        rows = [{'date': pd.Timestamp(d['date']), 'amount': d['amount']}
                for d in item['disclosures']]
        vc_disclosures[sc] = pd.DataFrame(rows)
        print(f"  {item['corp_name']} ({sc}): {len(rows)}건, net={item['net_amount']/1e8:,.0f}억")

# ── 차트 생성 ──
os.makedirs(OUTPUT_DIR, exist_ok=True)

for code, cfg in STOCKS.items():
    print(f"\n--- {cfg['name']} ({code}) ---")

    # IPO 정보
    ipo_row = ipo_df[ipo_df['code_num'] == code]
    if ipo_row.empty:
        print(f"  WARNING: No IPO data for {code}")
        continue
    ipo_row = ipo_row.iloc[0]
    offering_price = float(ipo_row['수정공모가'])
    listing_date = pd.to_datetime(ipo_row['상장일'])
    listing_close = float(ipo_row['상장일종가'])
    print(f"  상장일: {listing_date.date()}, 공모가: {offering_price:,.0f}, 상장일종가: {listing_close:,.0f}")

    # 주가 데이터
    sp = price_df[price_df['code_num'] == code].sort_values('날짜').copy()
    if cfg['period'] == '6m':
        end_date = listing_date + timedelta(days=183)
        sp = sp[sp['날짜'] <= end_date]
    print(f"  주가 데이터: {sp['날짜'].min().date()} ~ {sp['날짜'].max().date()} ({len(sp)}일)")

    # VC 누적 순매도 (정제된 JSON 데이터 사용)
    disc_df = vc_disclosures.get(code, pd.DataFrame(columns=['date', 'amount']))
    vc_daily = disc_df.groupby('date')['amount'].sum().sort_index()
    vc_cum = vc_daily.cumsum()
    vc_cum_억 = vc_cum / 1e8  # 억원 단위

    if cfg['period'] == '6m':
        vc_cum_억 = vc_cum_억[vc_cum_억.index <= end_date]

    # VC step function: 모든 거래일에 대해 전일 값 유지
    vc_step_dates = [sp['날짜'].iloc[0] - timedelta(days=1)]  # 시작점 (0)
    vc_step_vals = [0.0]
    for dt, val in vc_cum_억.items():
        vc_step_dates.append(dt)
        vc_step_vals.append(val)
    # 마지막 값을 차트 끝까지 연장
    vc_step_dates.append(sp['날짜'].iloc[-1])
    vc_step_vals.append(vc_step_vals[-1])

    final_vc_억 = abs(vc_step_vals[-1]) if vc_step_vals else 0
    print(f"  VC 누적 순매도: {final_vc_억:,.0f}억원 ({len(vc_cum_억)}일)")

    # ── 차트 그리기 ──
    fig, ax1 = plt.subplots(figsize=(15, 6))

    # 1) 주가 (좌축, 파란선)
    ax1.plot(sp['날짜'], sp['종가'], color='#4169E1', linewidth=1.5, label='수정주가', zorder=3)
    y_label_left = '수정주가 (원)'
    ax1.set_ylabel(y_label_left, color='#4169E1', fontsize=12)
    ax1.tick_params(axis='y', labelcolor='#4169E1')
    ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'{int(x):,}'))

    # 공모가 수평선
    ax1.axhline(y=offering_price, color='gray', linestyle='--', linewidth=0.8, zorder=1)
    # 공모가 레이블: 차트 왼쪽 하단에
    ax1.annotate(
        f'수정공모가 {int(offering_price):,}원',
        xy=(sp['날짜'].iloc[0], offering_price),
        xytext=(sp['날짜'].iloc[min(3, len(sp)-1)], offering_price * 0.93),
        fontsize=9, color='gray',
    )

    # 상장일종가 어노테이션 (알지노믹스 제외)
    if code != '476830':
        ax1.annotate(
            f'{int(listing_close):,}원',
            xy=(listing_date, listing_close),
            xytext=(listing_date + timedelta(days=5), listing_close * 1.03),
            fontsize=9, color='#4169E1',
            arrowprops=dict(arrowstyle='->', color='#4169E1', lw=0.8),
        )

    # 2) VC 누적 순매도 (우축, 빨간 step line + 핑크 fill)
    ax2 = ax1.twinx()

    if len(vc_step_dates) > 1:
        ax2.step(vc_step_dates, vc_step_vals, where='post',
                 color='#DC143C', linewidth=1.2, label='VC 누적 순매도 (억원)', zorder=2)
        ax2.fill_between(vc_step_dates, 0, vc_step_vals,
                         alpha=0.15, color='#DC143C', step='post')

        # 최종값 어노테이션 (차트 오른쪽 끝)
        ax2.annotate(
            f'{int(final_vc_억):,}억',
            xy=(vc_step_dates[-1], vc_step_vals[-1]),
            fontsize=10, color='#DC143C', fontweight='bold',
            ha='left', va='center',
        )

        # VC 매도일에 수직 점선
        for sell_date in vc_cum_억.index:
            ax1.axvline(x=sell_date, color='#FFB6C1', linestyle=':', linewidth=0.5, alpha=0.6, zorder=1)

    ax2.set_ylabel('VC 누적 순매도 (억원)', color='#DC143C', fontsize=12)
    ax2.tick_params(axis='y', labelcolor='#DC143C')

    # 우축 y축: 0이 아래, 음수(매도)가 위로
    # set_ylim(bottom, top)에서 bottom > top이면 축 반전
    if vc_step_vals:
        min_val = min(vc_step_vals)
        if min_val < 0:
            ax2.set_ylim(0, min_val * 1.12)  # 0(아래) → 음수(위)

    # 3) 알지노믹스 특수 어노테이션
    if code == '476830':
        ax1.annotate(
            '시초가 90,000원\n(수정공모가의 4배)',
            xy=(listing_date, 90000),
            xytext=(listing_date + timedelta(days=6), 70000),
            fontsize=9, color='#4169E1',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F0FE', edgecolor='#4169E1', alpha=0.8),
        )
        sell_mid = pd.Timestamp('2025-12-28')
        ax2.annotate(
            '3영업일간\n7개 VC 동시 매도\n(-872억)',
            xy=(pd.Timestamp('2025-12-23'), vc_step_vals[-1] * 0.6),
            xytext=(sell_mid + timedelta(days=8), vc_step_vals[-1] * 0.45),
            fontsize=9, color='#DC143C', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF0F0', edgecolor='#DC143C', alpha=0.8),
            arrowprops=dict(arrowstyle='->', color='#DC143C', lw=0.8),
        )

    # 4) X축 날짜 포맷
    if code == '476830':
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    else:
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    fig.autofmt_xdate()

    # 5) 제목 & 범례
    plt.title(cfg['title'], fontsize=14, fontweight='bold', pad=15)
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right', fontsize=9)
    ax1.grid(axis='y', alpha=0.3)

    plt.tight_layout()

    # 6) 저장
    out_path = os.path.join(OUTPUT_DIR, f'price_{code}.png')
    fig.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  → Saved: {out_path}")

print("\nAll charts generated!")
