---
jupytext:
  text_representation:
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 12. 其他参数曲线 Parametric Miscellany

本章收集了各种杂项参数曲线，包括蜗牛线、螺形线、以及其他独特的数学曲线。

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 120
plt.rcParams['axes.unicode_minus'] = False

def polar_to_xy(theta, r):
    return r * np.cos(theta), r * np.sin(theta)
```

## 12.1 蜗牛线 Cochleoid

$r = a\\frac{\\sin\\theta}{\\theta}$

```{code-cell} ipython3
theta = np.linspace(-6*np.pi, 6*np.pi, 6000)
theta = theta[theta != 0]  # avoid div by zero
a = 3
r = a * np.sin(theta) / theta
x, y = polar_to_xy(theta, r)
fig, ax = plt.subplots(figsize=(8,8))
ax.plot(x, y, linewidth=1)
ax.set_aspect('equal')
ax.set_title('Cochleoid / 蜗牛线')
ax.grid(True, alpha=0.3)
plt.show()
```

## 12.2 螺形线 Conchospiral

$r = a\\frac{\\mu^\\theta}{\\theta}$ — 对数螺旋与双曲螺旋的混合。

```{code-cell} ipython3
theta = np.linspace(0.5, 20, 4000)
a, mu, n = 1, 1.15, 1
r = a * mu**theta / theta**n
x, y = polar_to_xy(theta, r)
fig, ax = plt.subplots(figsize=(8,8))
ax.plot(x, y, 'darkred', linewidth=1)
ax.set_aspect('equal')
ax.set_title('Conchospiral / 螺形线')
ax.grid(True, alpha=0.3)
ax.set_xlim(-2, 2); ax.set_ylim(-2, 2)
plt.show()
```

## 12.3 等角螺线 Equiangular Spiral

$r = e^{a\theta}$ — 与对数螺旋相同。

```{code-cell} ipython3
theta = np.linspace(-8*np.pi, 4*np.pi, 6000)
a = 0.08
r = np.exp(a * theta)
x, y = polar_to_xy(theta, r)
fig, ax = plt.subplots(figsize=(8,8))
ax.plot(x, y, 'blue', linewidth=1)
ax.set_aspect('equal')
ax.set_title('Equiangular Spiral / 等角螺线')
ax.grid(True, alpha=0.3)
plt.show()
```

## 12.4 广义对数螺旋

$r = a^\\theta \\cdot b$ 的各种变体。

```{code-cell} ipython3
theta = np.linspace(0, 6*np.pi, 5000)
fig, axes = plt.subplots(1, 3, figsize=(15,5))
for ax, base in zip(axes, [1.05, 1.1, 1.2]):
    r = base**theta
    x, y = polar_to_xy(theta, r)
    ax.plot(x, y, linewidth=1)
    ax.set_aspect('equal')
    ax.set_title(f'$r = {base}^\\theta$')
    ax.grid(True, alpha=0.3)
plt.suptitle('Generalized Logarithmic Spirals', fontsize=14)
plt.tight_layout()
plt.show()
```

## 12.5 双参数参数曲线

$x = \\cos(at)\\cos(bt), \quad y = \\sin(at)\\cos(bt)$

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 4000)
fig, axes = plt.subplots(2, 3, figsize=(14, 9))
for idx, (a, b) in enumerate([(1,3), (2,3), (3,3), (1,5), (2,5), (3,5)]):
    ax = axes[idx//3][idx%3]
    x = np.cos(a*t) * np.cos(b*t)
    y = np.sin(a*t) * np.cos(b*t)
    ax.plot(x, y, linewidth=1.5)
    ax.set_aspect('equal')
    ax.set_title(f'$\\cos({a}t)\\cos({b}t), \\sin({a}t)\\cos({b}t)$')
    ax.grid(True, alpha=0.2)
plt.suptitle('Harmonic Product Curves', fontsize=14)
plt.tight_layout()
plt.show()
```

## 12.6 振荡圆周 Osculating Circle

在圆周上叠加强度递减的振荡波形。

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 5000)
R = 3
r = R + 0.5*np.sin(12*t)
x, y = polar_to_xy(t, r)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, linewidth=1)
ax.set_aspect('equal')
ax.set_title('Osculating Circle / 振荡圆周')
ax.grid(True, alpha=0.3)
plt.show()
```

## 12.7 螺线管形 Solenoid Curve

类似螺线管缠绕形状的 3D 投影模拟。

```{code-cell} ipython3
t = np.linspace(0, 8*np.pi, 5000)
R = 2
x = R * np.cos(t) + 0.3*np.cos(10*t)
y = R * np.sin(t) + 0.3*np.sin(10*t)
fig, ax = plt.subplots(figsize=(8,8))
ax.plot(x, y, 'darkgreen', linewidth=0.8)
ax.set_aspect('equal')
ax.set_title('Solenoid Curve (2D projection) / 螺线管曲线')
ax.grid(True, alpha=0.3)
plt.show()
```

## 12.8 参数乘积曲线

$x = \\cos t + \\cos k t, \quad y = \\sin t + \\sin k t$

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 5000)
fig, axes = plt.subplots(2, 3, figsize=(14, 9))
for idx, k in enumerate([2, 3, 4, 5, 7, 9]):
    ax = axes[idx//3][idx%3]
    x = np.cos(t) + np.cos(k*t)
    y = np.sin(t) + np.sin(k*t)
    ax.plot(x, y, linewidth=1.2)
    ax.set_aspect('equal')
    ax.set_title(f'$\\cos t+\\cos({k}t), \\sin t+\\sin({k}t)$')
    ax.grid(True, alpha=0.2)
plt.suptitle('Sum of Harmonics / 谐波叠加', fontsize=14)
plt.tight_layout()
plt.show()
```

## 12.9 立方菱形

$x = \\cos^3 t, \quad y = \\sin^3 t$ 与 $x = \\cos^3 t, y = \\sin^3 2t$

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 3000)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))
ax1.plot(np.cos(t)**3, np.sin(t)**3, linewidth=2)
ax1.set_aspect('equal'); ax1.set_title('$x=\\cos^3t, y=\\sin^3t$ (Astroid)')
ax1.grid(True, alpha=0.3)
ax2.plot(np.cos(t)**3, np.sin(2*t)**3, linewidth=2)
ax2.set_aspect('equal'); ax2.set_title('$x=\\cos^3t, y=\\sin^3(2t)$')
ax2.grid(True, alpha=0.3)
plt.tight_layout(); plt.show()
```

## 12.10 八角星 Eight Pointed Star

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 5000)
r = 1 + 0.5*np.cos(4*t)
x, y = polar_to_xy(t, r)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'orange', linewidth=2)
ax.set_aspect('equal')
ax.set_title('Eight Pointed Star / 八角星')
ax.grid(True, alpha=0.3); plt.show()
```
