# -*- coding: utf-8 -*-
"""313 clean 샘플 도출 funnel 도식 — Beaten by the Market 블로그용."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

rcParams["font.family"] = "Malgun Gothic"
rcParams["axes.unicode_minus"] = False

STEEL = "#4682B4"
STEEL_DK = "#2f5d8a"
STEEL_LT = "#a7c5e3"
GRAY = "#9aa3ab"
STAR = "#c0392b"

# (N, 라벨, 한줄설명)
stages = [
    (1813, "무상증자 전수", "데이터가이드 2010~2026 (중복 제거)"),
    (1161, "analysis_set", "상장 후 · DART 무상증자결정 공시 존재"),
    (478,  "비교가능", "T-1·T 둘 다 결산배당 있음 → 5분류 가능"),
    (313,  "clean  ★ 기본 분석집합", "직전·직후 사이 무상 외 자본변동 없음 (단일처치)"),
    (200,  "strict", "다른 무상증자도 없음 (강건성 확인용)"),
]
# 단계 사이 제외 (제외수, 설명)
drops = [
    (652, "상장 전 무상증자 제외\n(IPO 전·외국주 → 배당 비교 불가)"),
    (683, "T-1·T 결산배당 없음 제외\n(비배당·성장기업)"),
    (165, "무상 외 대형 자본변동 제외\n유상98·소각35·주식배당25·액면18·합병3·분할1"),
    (113, "다른 무상증자 동반 제외"),
]

fig, ax = plt.subplots(figsize=(10.5, 8.6))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis("off")

cx = 38                  # funnel 중심 x
maxw = 56                # 1813 일 때 너비
wmin = 16
nmax = stages[0][0]
def width(n):
    # sqrt 스케일(작은 단계도 보이게) + 하한
    return wmin + (maxw - wmin) * (n / nmax) ** 0.5

ytop = 89
ystep = 17.0
box_h = 9.0

colors = [STEEL_LT, STEEL, STEEL, STAR, STEEL_DK]
text_colors = ["#16334d", "white", "white", "white", "white"]

centers = []
for i, (n, label, desc) in enumerate(stages):
    w = width(n)
    yc = ytop - i * ystep
    centers.append(yc)
    x0 = cx - w / 2
    fc = colors[i]
    box = FancyBboxPatch((x0, yc - box_h / 2), w, box_h,
                         boxstyle="round,pad=0.4,rounding_size=1.2",
                         linewidth=2 if i == 3 else 1.2,
                         edgecolor=STAR if i == 3 else "white",
                         facecolor=fc, zorder=3)
    ax.add_patch(box)
    ax.text(cx, yc + 1.4, f"{n:,}", ha="center", va="center",
            fontsize=20, fontweight="bold", color=text_colors[i], zorder=4)
    ax.text(cx, yc - 2.6, label, ha="center", va="center",
            fontsize=11.5, fontweight="bold", color=text_colors[i], zorder=4)
    # 단계 설명(박스 아래 왼쪽)
    ax.text(cx - maxw / 2 - 2, yc, desc, ha="right", va="center",
            fontsize=9.2, color="#444", zorder=4)

# 단계 연결 화살표 + 제외 가지
for i, (drop_n, drop_desc) in enumerate(drops):
    y_from = centers[i] - box_h / 2
    y_to = centers[i + 1] + box_h / 2
    ax.add_patch(FancyArrowPatch((cx, y_from), (cx, y_to),
                 arrowstyle="-|>", mutation_scale=18,
                 linewidth=1.6, color="#6b7680", zorder=2))
    # 제외 가지 (오른쪽으로)
    ymid = (y_from + y_to) / 2 + 1.5
    bx = cx + maxw / 2 + 6
    ax.add_patch(FancyArrowPatch((cx + 1.5, ymid + 0.5), (bx - 1, ymid + 0.5),
                 arrowstyle="-|>", mutation_scale=12,
                 linewidth=1.3, color=GRAY, linestyle=(0, (4, 2)), zorder=2))
    ax.text(bx, ymid + 0.5, f"{drop_n:,}건 제외", ha="left", va="bottom",
            fontsize=12, fontweight="bold", color=STAR, zorder=4)
    ax.text(bx, ymid - 1.6, drop_desc, ha="left", va="top",
            fontsize=8.6, color="#555", zorder=4)

ax.text(cx, 99.2, "무상증자 1,813건 → 깨끗한 313건은 이렇게 걸러집니다",
        ha="center", va="top", fontsize=15, fontweight="bold", color="#16334d")

plt.tight_layout()
out = __file__.replace("make_funnel.py", "funnel_313.png")
plt.savefig(out, dpi=150, bbox_inches="tight")
print("saved:", out)
