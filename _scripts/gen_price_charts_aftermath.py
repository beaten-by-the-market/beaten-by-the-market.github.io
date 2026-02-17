"""
2026-02-16-kosdaq-ipo-vc-aftermath.md 포스팅용 주가 차트 생성 스크립트
주가 추이(파란선) + VC 누적 순매도(빨간 step line + 핑크 fill) 이중축 차트

데이터 처리: s5a_build_analysis_amt.py와 동일한 기준
  - parse_number()로 숫자 변환 (부호 보존)
  - Phase A: 신규상장 시점 VC 식별
  - Phase B: 해당 VC의 보통주 매매만 필터
  - signed_amount = MDF_SDK_CNT × HLD_UNT_PR
  - 상장 후 720일(2년) 이내만
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from datetime import timedelta
import re
import os

# ── 한글 폰트 설정 ──
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# ── 파일 경로 ──
STOCKS_DIR = r'C:\Users\Peter\Desktop\코스닥신규상장분석\stocks'
VC_RAW_CSV = r'C:\Users\Peter\Desktop\코스닥신규상장분석\krx_data\daeryang_hld_mth_ipo_2.5yr_vc_only.csv'
KOSDAQ_FILE = r'C:\Users\Peter\Desktop\코스닥신규상장분석\krx_data\kosdaq신규상장.xlsx'
IPO_CSV = r'C:\Users\Peter\Desktop\코스닥신규상장분석\docs\price_trade\data\ipo_analysis.csv'
OUTPUT_DIR = r'c:\Users\Peter\github\beaten-by-the-market.github.io\assets\images\2026-02-16-kosdaq-ipo-vc-aftermath'

# ── s5a_build_analysis_amt.py와 동일한 설정 ──
IPO_TYPES = [
    "신규상장(+)",
    "신규상장(무상취득)(+)",
    "신규상장(유상취득)(+)",
]
TRADE_TYPES = {
    "장내매도(-)": "장내매도",
    "장내매수(+)": "장내매수",
    "장외매도(-)": "장외매도",
    "장외매수(+)": "장외매수",
    "시간외매매(-)": "시간외매매",
    "시간외매매(+)": "시간외매매",
}
STK_KND_EQUITY = ["의결권있는 주식"]
MAX_DAYS = 720  # 2년

# ── 종목 설정 ──
STOCKS = {
    '377220': {
        'name': '프롬바이오',
        'title': '프롬바이오 — 주가 추이와 VC 누적 순매도',
    },
    '438700': {
        'name': '버넥트',
        'title': '버넥트 — 주가 추이와 VC 누적 순매도',
    },
    '393890': {
        'name': '더블유씨피',
        'title': '더블유씨피 — 주가 추이와 VC 누적 순매도',
    },
    '389030': {
        'name': '지니너스',
        'title': '지니너스 — 주가 추이와 VC 누적 순매도',
    },
    '274400': {
        'name': '이노시뮬레이션',
        'title': '이노시뮬레이션 — 주가 추이와 VC 누적 순매도',
    },
}


def parse_number(s):
    """s5a_build_analysis_amt.py와 동일한 숫자 파서.
    콤마 포맷 숫자 문자열 → int/float. '-' 등은 None.
    부호 보존: -40,000 → -40000
    비표준 폴백: 괄호, 원접미사, @접두사 등에서 숫자만 추출.
    """
    if pd.isna(s):
        return None
    s = str(s).strip().replace(",", "")
    if s in ("", "-", "(-)", "000"):
        return None
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            pass
    digits = re.findall(r'[\d.]+', s)
    if not digits:
        return None
    num_str = max(digits, key=len)
    if not num_str or num_str == ".":
        return None
    try:
        return int(num_str)
    except ValueError:
        try:
            return float(num_str)
        except ValueError:
            return None


# ── 데이터 로드 (s5a_build_analysis_amt.py와 동일한 방식) ──
print("Loading IPO analysis data...")
ipo_df = pd.read_csv(IPO_CSV)
ipo_df['code_num'] = ipo_df['코드'].astype(str).str.replace('A', '', regex=False)

print("Loading VC raw data (dtype=str)...")
df = pd.read_csv(VC_RAW_CSV, encoding="utf-8-sig", dtype=str)
df["stock_code"] = df["stock_code"].astype(str).str.zfill(6)
print(f"  → {len(df):,}행 전체")

# 숫자 변환 (parse_number 사용)
df["MDF_SDK_CNT"] = df["MDF_SDK_CNT"].apply(parse_number)
df["HLD_UNT_PR"] = df["HLD_UNT_PR"].apply(parse_number)

# 상장일 조인
print("Loading listing dates from kosdaq신규상장.xlsx...")
kosdaq = pd.read_excel(KOSDAQ_FILE)
kosdaq = kosdaq[["종목코드", "상장일"]].drop_duplicates()
kosdaq["종목코드"] = kosdaq["종목코드"].astype(str).str.zfill(6)
df = df.merge(
    kosdaq.rename(columns={"종목코드": "stock_code", "상장일": "LISTING_DATE"}),
    on="stock_code", how="left",
)

# ── Phase A: 신규상장 시점 VC 목록 ──
ipo_mask = df["HLD_MTH_ADJ"].isin(IPO_TYPES)
ipo_pairs = set(zip(df[ipo_mask]["SPC_NM"], df[ipo_mask]["stock_code"]))
print(f"Phase A: {len(ipo_pairs):,} (VC, 종목) 조합")

# ── Phase B: 해당 VC들의 보통주 매매 ──
trade_mask = (
    df["HLD_MTH_ADJ"].isin(TRADE_TYPES.keys())
    & df["STK_KND"].isin(STK_KND_EQUITY)
)
trade_df = df[trade_mask].copy()
trade_df["_pair"] = list(zip(trade_df["SPC_NM"], trade_df["stock_code"]))
trade_df = trade_df[trade_df["_pair"].isin(ipo_pairs)].copy()
trade_df = trade_df.drop(columns=["_pair"])

# 날짜 & 경과일
trade_df["listing_dt"] = pd.to_datetime(trade_df["LISTING_DATE"], format="%Y/%m/%d", errors="coerce")
trade_df["chg_dt"] = pd.to_datetime(trade_df["MDF_DT"], format="%Y.%m.%d", errors="coerce")
trade_df = trade_df.dropna(subset=["listing_dt", "chg_dt"])
trade_df["days"] = (trade_df["chg_dt"] - trade_df["listing_dt"]).dt.days

# 금액 산출: signed_amount = MDF_SDK_CNT × HLD_UNT_PR (부호 보존)
trade_df = trade_df.dropna(subset=["MDF_SDK_CNT", "HLD_UNT_PR"])
trade_df["signed_amount"] = trade_df["MDF_SDK_CNT"] * trade_df["HLD_UNT_PR"]

# 0~MAX_DAYS 범위만
trade_df = trade_df[(trade_df["days"] >= 0) & (trade_df["days"] <= MAX_DAYS)].copy()
print(f"Phase B: {len(trade_df):,}건 (보통주, Phase A VC, 0~{MAX_DAYS}일)")

# 대상 종목만 필터
trade_df = trade_df[trade_df["stock_code"].isin(STOCKS.keys())].copy()

# 매도 거래만 (signed_amount < 0)
sell_df = trade_df[trade_df["signed_amount"] < 0].copy()
print(f"  → 매도 거래: {len(sell_df):,}건")

# ── Per-stock VC summary ──
for code in STOCKS:
    sc = sell_df[sell_df['stock_code'] == code]
    total = sc['signed_amount'].sum() / 1e8
    n_vcs = sc['SPC_NM'].nunique()
    n_tx = len(sc)
    print(f"  {STOCKS[code]['name']} ({code}): {n_vcs}사, {n_tx}건, 순매도 {total:,.0f}억")

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
    end_date = listing_date + timedelta(days=MAX_DAYS)
    print(f"  상장일: {listing_date.date()}, 수정공모가: {offering_price:,.0f}, 상장일종가: {listing_close:,.0f}")
    print(f"  차트 범위: {listing_date.date()} ~ {end_date.date()} (2년)")

    # 주가 데이터 (per-stock CSV, 2년까지만)
    stock_csv = os.path.join(STOCKS_DIR, f'A{code}.csv')
    sp = pd.read_csv(stock_csv)
    sp['날짜'] = pd.to_datetime(sp['날짜'])
    sp = sp[(sp['날짜'] >= listing_date) & (sp['날짜'] <= end_date)].sort_values('날짜')
    print(f"  주가 데이터: {sp['날짜'].min().date()} ~ {sp['날짜'].max().date()} ({len(sp)}일)")

    # VC 누적 순매도 (signed_amount < 0, 이미 2년 필터 적용됨)
    sc_sell = sell_df[sell_df['stock_code'] == code]
    vc_daily = sc_sell.groupby('chg_dt')['signed_amount'].sum().sort_index()
    vc_cum = vc_daily.cumsum()
    vc_cum_억 = vc_cum / 1e8

    # VC step function
    vc_step_dates = [sp['날짜'].iloc[0] - timedelta(days=1)]
    vc_step_vals = [0.0]
    for dt, val in vc_cum_억.items():
        vc_step_dates.append(dt)
        vc_step_vals.append(val)
    vc_step_dates.append(sp['날짜'].iloc[-1])
    vc_step_vals.append(vc_step_vals[-1])

    final_vc_억 = abs(vc_step_vals[-1]) if vc_step_vals else 0
    print(f"  VC 누적 순매도: {final_vc_억:,.0f}억원 ({len(vc_cum_억)}건)")

    # ── 차트 그리기 ──
    fig, ax1 = plt.subplots(figsize=(15, 6))

    # 1) 주가 (좌축, 파란선)
    ax1.plot(sp['날짜'], sp['종가'], color='#4169E1', linewidth=1.5, label='수정주가', zorder=3)
    ax1.set_ylabel('수정주가 (원)', color='#4169E1', fontsize=12)
    ax1.tick_params(axis='y', labelcolor='#4169E1')
    ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'{int(x):,}'))

    # 공모가 수평선
    ax1.axhline(y=offering_price, color='gray', linestyle='--', linewidth=0.8, zorder=1)
    ax1.annotate(
        f'수정공모가 {int(offering_price):,}원',
        xy=(sp['날짜'].iloc[0], offering_price),
        xytext=(sp['날짜'].iloc[min(3, len(sp)-1)], offering_price * 0.90),
        fontsize=9, color='gray',
    )

    # 상장일종가 어노테이션
    ax1.annotate(
        f'{int(listing_close):,}원',
        xy=(listing_date, listing_close),
        xytext=(listing_date + timedelta(days=20), listing_close * 1.06),
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

        ax2.annotate(
            f'-{int(final_vc_억):,}억',
            xy=(vc_step_dates[-1], vc_step_vals[-1]),
            fontsize=10, color='#DC143C', fontweight='bold',
            ha='left', va='center',
        )

        for sell_date in vc_cum_억.index:
            ax1.axvline(x=sell_date, color='#FFB6C1', linestyle=':', linewidth=0.5, alpha=0.6, zorder=1)

    ax2.set_ylabel('VC 누적 순매도 (억원)', color='#DC143C', fontsize=12)
    ax2.tick_params(axis='y', labelcolor='#DC143C')

    if vc_step_vals:
        min_val = min(vc_step_vals)
        if min_val < 0:
            ax2.set_ylim(0, min_val * 1.12)

    # X축 날짜 포맷
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    fig.autofmt_xdate()

    # 제목 & 범례
    plt.title(cfg['title'], fontsize=14, fontweight='bold', pad=15)
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right', fontsize=9)
    ax1.grid(axis='y', alpha=0.3)

    plt.tight_layout()

    out_path = os.path.join(OUTPUT_DIR, f'price_{code}.png')
    fig.savefig(out_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  → Saved: {out_path}")

print("\nAll charts generated!")
