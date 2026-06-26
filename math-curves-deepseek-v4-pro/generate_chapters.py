"""
Generate all 12 mathematical curve Jupyter notebooks for Jupyter Book.
"""
import json, os

OUT = 'D:/work_claude/wmt_mathgv_matplotlib_study-master'

def make_nb(cells, filename):
    nb = {
        'nbformat': 4,
        'nbformat_minor': 5,
        'metadata': {
            'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'},
            'language_info': {'name': 'python', 'version': '3.10.0'}
        },
        'cells': cells
    }
    path = os.path.join(OUT, filename)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f'  Created: {filename}')

def md(src):
    if isinstance(src, str):
        src = src.splitlines(True)
    return {'cell_type': 'markdown', 'metadata': {}, 'source': src}

def code(src):
    if isinstance(src, str):
        src = src.splitlines(True)
    return {'cell_type': 'code', 'metadata': {}, 'source': src, 'outputs': [], 'execution_count': None}

# Shared imports
IMPORTS = """import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, tan, pi, exp, sqrt, atan, cosh, sinh

plt.rcParams['figure.dpi'] = 120
plt.rcParams['axes.unicode_minus'] = False

def polar_to_xy(theta, r):
    return r * np.cos(theta), r * np.sin(theta)

def finite_xy(x, y):
    mask = np.isfinite(x) & np.isfinite(y)
    return x[mask], y[mask]
"""

print("Generating all 12 chapter notebooks + intro...")
print("="*50)

# =====================================================
# Chapter 1: Conic Sections (7 curves)
# =====================================================
make_nb([
    md("""# 1. 圆锥曲线 Conic Sections

圆、椭圆、抛物线、双曲线 — 用平面截圆锥所得的四类曲线，以及退化情形。"""),
    code(IMPORTS),
    md("""## 1.1 圆 Circle

$$x = r\\cos(t), \\quad y = r\\sin(t)$$"""),
    code("""t = np.linspace(0, 2*np.pi, 1000)
fig, ax = plt.subplots(figsize=(6,6))
ax.plot(np.cos(t), np.sin(t), 'b-', linewidth=2)
ax.set_aspect('equal')
ax.set_title('Circle / 圆')
ax.grid(True, alpha=0.3)
plt.show()"""),
    md("""## 1.2 椭圆 Ellipse

$$x = a\\cos(t), \\quad y = b\\sin(t)$$

展示不同长短轴比率的椭圆。"""),
    code("""t = np.linspace(0, 2*np.pi, 1000)
fig, ax = plt.subplots(figsize=(8,5))
ax.plot(2*np.cos(t), 1*np.sin(t), 'r-', linewidth=2, label='a=2, b=1')
ax.plot(1.5*np.cos(t), 0.7*np.sin(t), 'g--', linewidth=2, label='a=1.5, b=0.7')
ax.plot(1.2*np.cos(t), 1.2*np.sin(t), 'b-.', linewidth=2, label='a=1.2, b=1.2')
ax.set_aspect('equal')
ax.set_title('Ellipse / 椭圆')
ax.legend()
ax.grid(True, alpha=0.3)
plt.show()"""),
    md("""## 1.3 抛物线 Parabola

$$y = ax^2$$"""),
    code("""x = np.linspace(-4, 4, 1000)
fig, axes = plt.subplots(1, 3, figsize=(15,4))
for ax_cur, a, lbl in zip(axes, [0.5, 1.0, 2.0], ['a=0.5', 'a=1', 'a=2']):
    ax_cur.plot(x, a*x**2, linewidth=2)
    ax_cur.set_title(f'$y = {a}x^2$')
    ax_cur.set_aspect('equal')
    ax_cur.grid(True, alpha=0.3)
plt.suptitle('Parabola / 抛物线')
plt.tight_layout()
plt.show()"""),
    md("""## 1.4 反比例 / 直角双曲线 Rectangular Hyperbola

$$y = \\frac{1}{x}$$"""),
    code("""x = np.r_[np.linspace(-4, -0.05, 500), np.nan, np.linspace(0.05, 4, 500)]
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, 1/x, 'b-', linewidth=2)
ax.axhline(0, color='gray', linewidth=0.5, linestyle='--')
ax.axvline(0, color='gray', linewidth=0.5, linestyle='--')
ax.set_title('Rectangular Hyperbola: $y=1/x$')
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_ylim(-6, 6)
plt.show()"""),
    md("""## 1.5 双曲线 Hyperbola

$$\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1$$"""),
    code("""a, b = 2, 1
t = np.linspace(-2.5, 2.5, 1000)
x_pos = a * np.cosh(t)
y_pos = b * np.sinh(t)
x_neg = -a * np.cosh(t)
y_neg = b * np.sinh(t)
fig, ax = plt.subplots(figsize=(8,8))
ax.plot(x_pos, y_pos, 'b-', linewidth=2)
ax.plot(x_neg, y_neg, 'b-', linewidth=2)
asx = np.linspace(-6, 6, 100)
ax.plot(asx, (b/a)*asx, 'gray', linewidth=0.8, linestyle='--', label='Asymptotes')
ax.plot(asx, -(b/a)*asx, 'gray', linewidth=0.8, linestyle='--')
ax.set_title(r'$\\frac{x^2}{4} - y^2 = 1$')
ax.set_aspect('equal')
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_xlim(-6, 6)
ax.set_ylim(-4, 4)
plt.show()"""),
    md("""## 1.6 退化圆锥 Degenerate Conics

交叉线 $y^2 = x^2$ 和平行线 $x^2 = 1$。"""),
    code("""x = np.linspace(-4, 4, 100)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5))
ax1.plot(x, x, 'r-', linewidth=2, label='y = x')
ax1.plot(x, -x, 'b-', linewidth=2, label='y = -x')
ax1.set_title('$y^2=x^2$ — Intersecting Lines')
ax1.set_aspect('equal')
ax1.legend()
ax1.grid(True, alpha=0.3)
ax2.axvline(1, color='g', linewidth=3)
ax2.axvline(-1, color='g', linewidth=3)
ax2.set_title('$x^2=1$ — Parallel Lines')
ax2.set_aspect('equal')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(-3, 3)
ax2.set_ylim(-2, 2)
plt.tight_layout()
plt.show()"""),
    md("""## 1.7 单位双曲线 — $xy = 1$

旋转45度的双曲线。"""),
    code("""x = np.r_[np.linspace(-4, -0.1, 500), np.nan, np.linspace(0.1, 4, 500)]
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, 1/x, 'purple', linewidth=2)
ax.axhline(0, color='gray', ls='--', lw=0.5)
ax.axvline(0, color='gray', ls='--', lw=0.5)
ax.set_title('Unit Hyperbola: $xy = 1$')
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
plt.show()"""),
], '01_conic_sections.ipynb')
print("Chapter 1 done")
