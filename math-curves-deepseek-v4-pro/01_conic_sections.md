---
jupytext:
  text_representation:
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 圆锥曲线 Conic Sections

圆锥曲线是平面截圆锥所得的曲线，包含圆、椭圆、抛物线、双曲线四大类。

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 120
plt.rcParams['axes.unicode_minus'] = False
```

## 1.1 圆 Circle

$x = r \cos(t), \quad y = r \sin(t)$

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 1000)
r = 1
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(r * np.cos(t), r * np.sin(t), 'b-', linewidth=2)
ax.set_aspect('equal')
ax.set_title('Circle / 圆')
ax.grid(True, alpha=0.3)
plt.show()
```

## 1.2 椭圆 Ellipse

$x = a \cos(t), \quad y = b \sin(t)$

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 1000)
a, b = 2.0, 1.0
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(a * np.cos(t), b * np.sin(t), 'r-', linewidth=2, label='a=2, b=1')
ax.plot(1.5 * np.cos(t), 0.7 * np.sin(t), 'g--', linewidth=2, label='a=1.5, b=0.7')
ax.set_aspect('equal')
ax.set_title('Ellipse / 椭圆')
ax.legend()
ax.grid(True, alpha=0.3)
plt.show()
```

## 1.3 抛物线 Parabola

$y = ax^2$

```{code-cell} ipython3
x = np.linspace(-4, 4, 1000)
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, a, lbl in zip(axes, [0.5, 1.0, 2.0], ['a=0.5', 'a=1', 'a=2']):
    ax.plot(x, a * x**2, linewidth=2)
    ax.set_title(f'Parabola y={a}x²')
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
plt.suptitle('Parabola / 抛物线')
plt.tight_layout()
plt.show()
```

## 1.4 直角双曲线 Rectangular Hyperbola

$y = 1/x$

```{code-cell} ipython3
x1 = np.linspace(-4, -0.05, 500)
x2 = np.linspace(0.05, 4, 500)
fig, ax = plt.subplots(figsize=(7, 7))
ax.plot(x1, 1/x1, 'b-', linewidth=2)
ax.plot(x2, 1/x2, 'b-', linewidth=2)
ax.axhline(0, color='gray', linewidth=0.5, linestyle='--')
ax.axvline(0, color='gray', linewidth=0.5, linestyle='--')
ax.set_title('Rectangular Hyperbola: $y = 1/x$')
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_ylim(-6, 6)
plt.show()
```

## 1.5 双曲线 Hyperbola

$\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$

```{code-cell} ipython3
a, b = 2, 1
t = np.linspace(-2.5, 2.5, 1000)
x_pos = a * np.cosh(t)
y_pos = b * np.sinh(t)
x_neg = -a * np.cosh(t)
y_neg = b * np.sinh(t)

fig, ax = plt.subplots(figsize=(8, 8))
ax.plot(x_pos, y_pos, 'b-', linewidth=2, label='Hyperbola')
ax.plot(x_neg, y_neg, 'b-', linewidth=2)
asym_x = np.linspace(-6, 6, 100)
ax.plot(asym_x, (b/a)*asym_x, 'gray', linewidth=0.8, linestyle='--', label='Asymptotes')
ax.plot(asym_x, -(b/a)*asym_x, 'gray', linewidth=0.8, linestyle='--')
ax.set_title(r'Hyperbola: $\frac{x^2}{4} - y^2 = 1$')
ax.set_aspect('equal')
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_xlim(-6, 6)
ax.set_ylim(-4, 4)
plt.show()
```

## 1.6 退化圆锥 Degenerate Conics

相交直线：$y^2 = x^2$ 和 平行线：$x^2 = 1$

```{code-cell} ipython3
x = np.linspace(-4, 4, 100)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(x, x, 'r-', linewidth=2, label='y = x')
ax1.plot(x, -x, 'b-', linewidth=2, label='y = -x')
ax1.set_title('Intersecting Lines: $y^2=x^2$')
ax1.set_aspect('equal')
ax1.legend()
ax1.grid(True, alpha=0.3)
ax2.axvline(1, color='g', linewidth=3, label='x = 1')
ax2.axvline(-1, color='g', linewidth=3)
ax2.set_title('Parallel Lines: $x^2=1$')
ax2.set_aspect('equal')
ax2.legend()
ax2.grid(True, alpha=0.3)
ax2.set_xlim(-3, 3)
ax2.set_ylim(-2, 2)
plt.tight_layout()
plt.show()
```

## 1.7 单位双曲线 Unit Hyperbola

$xy = 1$ 旋转45°的双曲线

```{code-cell} ipython3
t = np.linspace(-4, 4, 1000)
fig, ax = plt.subplots(figsize=(8, 6))
x = np.r_[np.linspace(-4, -0.15, 500), np.nan, np.linspace(0.15, 4, 500)]
ax.plot(x, 1/x, 'purple', linewidth=2)
ax.axhline(0, color='gray', linewidth=0.5, linestyle='--')
ax.axvline(0, color='gray', linewidth=0.5, linestyle='--')
ax.set_title('Unit Hyperbola: $xy = 1$')
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_ylim(-6, 6)
ax.set_xlim(-6, 6)
plt.show()
```
