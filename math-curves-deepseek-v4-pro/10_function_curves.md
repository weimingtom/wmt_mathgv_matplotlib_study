---
jupytext:
  text_representation:
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 10. 经典函数曲线 Function Curves

三角函数、指数函数、对数函数、正态分布曲线等经典数学函数。

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 120
plt.rcParams['axes.unicode_minus'] = False
```

## 10.1 正弦曲线 Sine

$y = \sin x$

```{code-cell} ipython3
x = np.linspace(-4*np.pi, 4*np.pi, 2000)
fig, ax = plt.subplots(figsize=(14, 5))
ax.plot(x, np.sin(x), 'b-', linewidth=2, label='$y=\\sin x$')
ax.axhline(0, color='gray', lw=0.5); ax.grid(True, alpha=0.3)
ax.set_title('Sine Curve / 正弦曲线'); ax.legend()
ax.set_xlim(-4*np.pi, 4*np.pi); ax.set_ylim(-1.5, 1.5); plt.show()
```

## 10.2 余弦与正切 Cosine & Tangent

```{code-cell} ipython3
x = np.linspace(-2*np.pi, 2*np.pi, 2000)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
ax1.plot(x, np.cos(x), 'orange', linewidth=2, label='$y=\\cos x$')
ax1.set_title('Cosine Curve'); ax1.grid(True, alpha=0.3); ax1.legend()
x2 = np.linspace(-np.pi/2+0.1, np.pi/2-0.1, 500)
ax2.plot(x2, np.tan(x2), 'r-', linewidth=2, label='$y=\\tan x$')
ax2.plot(x2+np.pi, np.tan(x2), 'r-', linewidth=2)
ax2.set_title('Tangent Curve'); ax2.grid(True, alpha=0.3)
ax2.set_ylim(-8, 8); ax2.legend()
plt.tight_layout(); plt.show()
```

## 10.3 指数函数 Exponential

$y = e^x$ 及其反射 $y = e^{-x}$

```{code-cell} ipython3
x = np.linspace(-4, 4, 2000)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, np.exp(x), 'r-', linewidth=2, label='$y=e^x$')
ax.plot(x, np.exp(-x), 'b-', linewidth=2, label='$y=e^{-x}$')
ax.axhline(0, color='gray', lw=0.5); ax.axhline(1, color='gray', ls=':', lw=0.5)
ax.set_title('Exponential Functions / 指数函数'); ax.grid(True, alpha=0.3)
ax.set_ylim(-1, 8); ax.legend(); plt.show()
```

## 10.4 对数函数 Logarithm

$y = \ln x$ 和 $y = \log_{10} x$

```{code-cell} ipython3
x = np.linspace(0.01, 8, 2000)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, np.log(x), 'g-', linewidth=2, label='$y=\\ln x$')
ax.plot(x, np.log10(x), 'b-', linewidth=2, label='$y=\\log_{10} x$')
ax.set_title('Logarithmic Functions / 对数函数'); ax.grid(True, alpha=0.3)
ax.legend(); plt.show()
```

## 10.5 高斯曲线 / 正态分布 Gaussian

$y = \\frac{1}{\\sigma\\sqrt{2\\pi}} e^{-x^2/(2\\sigma^2)}$

```{code-cell} ipython3
x = np.linspace(-6, 6, 2000)
fig, ax = plt.subplots(figsize=(10, 6))
for sigma in [0.5, 1.0, 1.5, 2.0]:
    y = 1/(sigma*np.sqrt(2*np.pi)) * np.exp(-x**2/(2*sigma**2))
    ax.plot(x, y, linewidth=2, label=f'$\\sigma={sigma}$')
ax.set_title('Normal Distribution / 正态分布'); ax.grid(True, alpha=0.3)
ax.legend(); plt.show()
```

## 10.6 误差函数 Error Function

$\operatorname{erf}(x) = \\frac{2}{\\sqrt{\\pi}}\\int_0^x e^{-t^2}dt$

```{code-cell} ipython3
from scipy.special import erf
x = np.linspace(-4, 4, 2000)
y = erf(x)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, 'purple', linewidth=2)
ax.axhline(0, color='gray', lw=0.5); ax.grid(True, alpha=0.3)
ax.set_title('Error Function / 误差函数'); ax.set_ylim(-1.2, 1.2)
plt.show()
```

## 10.7 Sinc 函数

$\operatorname{sinc}(x) = \\frac{\\sin x}{x}$

```{code-cell} ipython3
x = np.r_[np.linspace(-20, -0.001, 2000), np.linspace(0.001, 20, 2000)]
y = np.sin(x) / x
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(x, y, 'darkred', linewidth=1.5)
ax.set_title('Sinc Function: $\\sin x / x$'); ax.grid(True, alpha=0.3)
ax.set_xlim(-20, 20); plt.show()
```

## 10.8 Sigmoid 函数

$\sigma(x) = \\frac{1}{1 + e^{-x}}$

```{code-cell} ipython3
x = np.linspace(-8, 8, 2000)
y = 1 / (1 + np.exp(-x))
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, 'teal', linewidth=2)
ax.axhline(0, color='gray', lw=0.5); ax.axhline(1, color='gray', ls='--', lw=0.5)
ax.set_title('Sigmoid Function / S型函数'); ax.grid(True, alpha=0.3)
ax.set_ylim(-0.1, 1.1); plt.show()
```

## 10.9 阻尼振荡 Damped Oscillation

$y = e^{-0.1x} \sin x$

```{code-cell} ipython3
x = np.linspace(0, 30, 3000)
y = np.exp(-0.1*x) * np.sin(x)
fig, ax = plt.subplots(figsize=(14, 5))
ax.plot(x, y, 'b-', linewidth=1.5, label='$e^{-0.1x}\\sin x$')
ax.plot(x, np.exp(-0.1*x), 'r--', linewidth=1, label='Envelope $\\pm e^{-0.1x}$')
ax.plot(x, -np.exp(-0.1*x), 'r--', linewidth=1)
ax.set_title('Damped Oscillation / 阻尼振荡'); ax.grid(True, alpha=0.3)
ax.legend(); plt.show()
```

## 10.10 贝塞尔曲线 Bezier Curve

三次贝塞尔曲线示例。

```{code-cell} ipython3
def bezier(p0, p1, p2, p3, n=200):
    t = np.linspace(0, 1, n)
    x = (1-t)**3*p0[0] + 3*(1-t)**2*t*p1[0] + 3*(1-t)*t**2*p2[0] + t**3*p3[0]
    y = (1-t)**3*p0[1] + 3*(1-t)**2*t*p1[1] + 3*(1-t)*t**2*p2[1] + t**3*p3[1]
    return x, y

fig, ax = plt.subplots(figsize=(8,8))
ctrl_pts = [(0,0), (2,4), (6,4), (8,0)]
x, y = bezier(*ctrl_pts)
ax.plot(x, y, 'b-', linewidth=2, label='Bezier Curve')
cx, cy = zip(*ctrl_pts)
ax.plot(cx, cy, 'ro--', markersize=8, linewidth=1, label='Control Points')
ax.set_aspect('equal'); ax.set_title('Cubic Bezier Curve / 贝塞尔曲线')
ax.legend(); ax.grid(True, alpha=0.3); plt.show()
```

## 10.11 参数贝塞尔曲线

多个控制点的复杂贝塞尔形状。

```{code-cell} ipython3
fig, axes = plt.subplots(1, 3, figsize=(15,5))
curves = [
    [(0,0), (1,5), (4,5), (5,0), (5,-3), (2,-2), (0,0)],
    [(0,0), (3,4), (1,5), (4,5), (5,3), (3,1), (5,0)],
    [(0,3), (2,5), (4,5), (5,3), (4,1), (2,0), (0,1)]
]
for ax, ctrl in zip(axes, curves):
    for i in range(0, len(ctrl)-3, 3):
        bx, by = bezier(ctrl[i], ctrl[i+1], ctrl[i+2], ctrl[i+3])
        ax.plot(bx, by, linewidth=2)
    cx, cy = zip(*ctrl)
    ax.plot(cx, cy, 'o--', markersize=6, linewidth=0.5)
    ax.set_aspect('equal'); ax.grid(True, alpha=0.2)
plt.suptitle('Bezier Curve Variations', fontsize=14)
plt.tight_layout(); plt.show()
```

## 10.12 Beta 分布曲线

$B(x|\\alpha,\\beta) = \\frac{x^{\\alpha-1}(1-x)^{\\beta-1}}{B(\\alpha,\\beta)}$

```{code-cell} ipython3
from scipy.special import beta as beta_func
x = np.linspace(0.01, 0.99, 2000)
fig, ax = plt.subplots(figsize=(10, 6))
for alpha, beta_val, ls in [(2,2,'-'), (3,3,'--'), (2,5,'-.'), (5,2,':')]:
    y = x**(alpha-1) * (1-x)**(beta_val-1) / beta_func(alpha, beta_val)
    ax.plot(x, y, linewidth=2, linestyle=ls, label=f'Beta({alpha},{beta_val})')
ax.set_title('Beta Distribution / Beta分布')
ax.grid(True, alpha=0.3); ax.legend(); plt.show()
```
