---
jupytext:
  text_representation:
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 7. 代数曲线 Algebraic Curves

由多项式方程 $F(x,y)=0$ 定义的平面曲线，是最古老、最重要的曲线家族之一。

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 120
plt.rcParams['axes.unicode_minus'] = False
```

## 7.1 伯努利双纽线 Lemniscate of Bernoulli

$r^2 = a^2\cos(2\theta)$ — 形似无穷符号 $\infty$

```{code-cell} ipython3
theta = np.linspace(0, 2*np.pi, 3000)
a = 1
r2 = np.cos(2*theta)
r = np.where(r2 >= 0, np.sqrt(np.abs(r2)), np.nan)
x, y = r*np.cos(theta), r*np.sin(theta)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'b-', linewidth=2)
ax.fill(x, y, alpha=0.2, color='blue')
ax.set_aspect('equal')
ax.set_title('Lemniscate: $r^2=\\cos(2\\theta)$')
ax.grid(True, alpha=0.3)
plt.show()
```

## 7.2 蔓叶线 Cissoid of Diocles

$y^2 = \\frac{x^3}{2a - x}$

```{code-cell} ipython3
a = 1.0
x = np.linspace(0.001, 2*a - 0.01, 2000)
y = np.sqrt(x**3 / (2*a - x))
fig, ax = plt.subplots(figsize=(8,8))
ax.plot(x, y, 'g-', linewidth=2, label='Cissoid')
ax.plot(x, -y, 'g-', linewidth=2)
ax.axvline(x=2*a, color='gray', linewidth=1, linestyle='--', label='x=2a Asymptote')
ax.set_aspect('equal')
ax.set_title('Cissoid of Diocles / 蔓叶线')
ax.legend(); ax.grid(True, alpha=0.3)
ax.set_xlim(0, 3); ax.set_ylim(-3, 3)
plt.show()
```

## 7.3 阿涅西的女巫 Witch of Agnesi

$y = \\frac{8a^3}{x^2 + 4a^2}$

```{code-cell} ipython3
x = np.linspace(-8, 8, 2000)
a = 1
y = 8*a**3 / (x**2 + 4*a**2)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, 'purple', linewidth=2)
ax.fill_between(x, y, alpha=0.2, color='purple')
ax.set_title('Witch of Agnesi / 阿涅西的女巫')
ax.grid(True, alpha=0.3)
ax.set_xlim(-8, 8); ax.set_ylim(0, 2.5)
plt.show()
```

## 7.4 笛卡尔叶形线 Folium of Descartes

$x^3 + y^3 = 3axy$

```{code-cell} ipython3
theta = np.linspace(-np.pi/2 + 0.15, np.pi/2 - 0.15, 2000)
a = 1
r = 3*a*np.sin(theta)*np.cos(theta) / (np.sin(theta)**3 + np.cos(theta)**3)
x, y = r*np.cos(theta), r*np.sin(theta)
fig, ax = plt.subplots(figsize=(8,8))
ax.plot(x, y, 'r-', linewidth=2)
asym = np.linspace(-3, 3, 100)
ax.plot(asym, -asym - a, 'gray', linewidth=0.8, linestyle='--')
ax.set_aspect('equal')
ax.set_title('Folium of Descartes / 笛卡尔叶形线')
ax.grid(True, alpha=0.3)
ax.set_xlim(-3, 3); ax.set_ylim(-3, 3)
plt.show()
```

## 7.5 十字线 / 蛇形线 Serpentine

$y = \\frac{abx}{x^2 + a^2}$

```{code-cell} ipython3
x = np.linspace(-8, 8, 2000)
a, b = 2, 3
y = a*b*x / (x**2 + a**2)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, 'teal', linewidth=2)
ax.axhline(0, color='gray', linewidth=0.5, linestyle='--')
ax.set_title('Serpentine Curve / 蛇形线')
ax.grid(True, alpha=0.3)
plt.show()
```

## 7.6 双扭线 / 8字曲线 Figure-Eight

$y^2 = x(a^2 - x^2)$

```{code-cell} ipython3
a = 2
x = np.linspace(-a, a, 2000)
y = np.sqrt(np.maximum(x*(a**2 - x**2), 0))
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(x, y, 'blue', linewidth=2)
ax.plot(x, -y, 'blue', linewidth=2)
ax.set_aspect('equal')
ax.set_title('Figure-Eight Curve / 双扭线')
ax.grid(True, alpha=0.3)
plt.show()
```

## 7.7 三次曲线 / 立方抛物线 Cubic Parabola

$y = x^3$

```{code-cell} ipython3
x = np.linspace(-4, 4, 2000)
y = x**3
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(x, y, 'darkorange', linewidth=2)
ax.axhline(0, color='gray', linewidth=0.5, linestyle='-')
ax.axvline(0, color='gray', linewidth=0.5, linestyle='-')
ax.set_title('Cubic Parabola: $y = x^3$')
ax.grid(True, alpha=0.3)
plt.show()
```

## 7.8 半立方抛物线 Semicubical Parabola

$y^2 = ax^3$

```{code-cell} ipython3
a = 1
x = np.linspace(0, 5, 2000)
y = np.sqrt(a * x**3)
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(x, y, 'red', linewidth=2, label='$y^2=x^3$')
ax.plot(x, -y, 'red', linewidth=2)
ax.set_aspect('equal')
ax.set_title('Semicubical Parabola / 半立方抛物线')
ax.legend(); ax.grid(True, alpha=0.3)
plt.show()
```

## 7.9 奇诺曲线 / 拐线

$y = x^4 - 3x^2$ — 有两个极小的四次曲线

```{code-cell} ipython3
x = np.linspace(-2.5, 2.5, 2000)
y = x**4 - 3*x**2
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(x, y, 'green', linewidth=2)
ax.set_title('Quartic: $y = x^4 - 3x^2$')
ax.grid(True, alpha=0.3)
plt.show()
```

## 7.10 珍珠线 Pearl Curve

$x^2 + y^2 = a^2x^2y^2$ — 代数曲线的复杂形式

```{code-cell} ipython3
a = 1.5
x = np.linspace(-3, 3, 400)
y = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x, y)
F = X**2 + Y**2 - a**2*X**2*Y**2
fig, ax = plt.subplots(figsize=(7,7))
ax.contour(X, Y, F, levels=[0], colors=['navy'], linewidths=1.5)
ax.set_aspect('equal')
ax.set_title('Pearl Curve / 珍珠线')
ax.grid(True, alpha=0.3)
ax.set_xlim(-3, 3); ax.set_ylim(-3, 3)
plt.show()
```

## 7.11 三次方程 Trident

$xy = x^3 - 1$ 形式的曲线。

```{code-cell} ipython3
x1 = np.linspace(-3, -0.05, 500)
x2 = np.linspace(0.05, 3, 500)
fig, ax = plt.subplots(figsize=(8,6))
for x_arr in [x1, x2]:
    y = (x_arr**3 - 1) / x_arr
    ax.plot(x_arr, y, 'purple', linewidth=2)
ax.axhline(0, color='gray', ls='--', lw=0.5)
ax.axvline(0, color='gray', ls='--', lw=0.5)
ax.set_title('Trident Curve: $xy = x^3 - 1$')
ax.grid(True, alpha=0.3)
ax.set_ylim(-10, 10)
plt.show()
```

## 7.12 四次曲线 Bicorn

$y^2(a^2 - x^2) = (x^2 + 2ay - a^2)^2$

```{code-cell} ipython3
a = 2
x = np.linspace(-a, a, 400)
y = np.linspace(-a, 3, 400)
X, Y = np.meshgrid(x, y)
F = Y**2 * (a**2 - X**2) - (X**2 + 2*a*Y - a**2)**2
fig, ax = plt.subplots(figsize=(7,7))
ax.contour(X, Y, F, levels=[0], colors=['darkred'], linewidths=1.5)
ax.set_aspect('equal')
ax.set_title('Bicorn Curve / 双角线')
ax.grid(True, alpha=0.3)
plt.show()
```

## 7.13 三叉线 Trident of Newton

$xy = ax^3 + bx^2 + cx + d$

```{code-cell} ipython3
def newton_trident(a,b,c,d, xlim=(-4,4), ylim=(-8,8)):
    x1 = np.linspace(xlim[0], -0.02, 500)
    x2 = np.linspace(0.02, xlim[1], 500)
    fig, ax = plt.subplots(figsize=(7,7))
    for x_arr in [x1, x2]:
        y = (a*x_arr**3 + b*x_arr**2 + c*x_arr + d) / x_arr
        ax.plot(x_arr, y, linewidth=2)
    ax.axhline(0, color='gray', ls='--', lw=0.5)
    ax.axvline(0, color='gray', ls='--', lw=0.5)
    ax.set_aspect('equal')
    ax.set_title("Newton's Trident")
    ax.grid(True, alpha=0.3)
    ax.set_ylim(ylim)
    plt.show()

newton_trident(1, 0, -3, 1)
```

## 7.14 双曲正弦/余弦曲线

$y = \cosh x$ 和 $y = \sinh x$

```{code-cell} ipython3
x = np.linspace(-3, 3, 1000)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(x, np.cosh(x), 'b-', linewidth=2)
ax1.set_title('$y = \\cosh x$')
ax1.grid(True, alpha=0.3)
ax2.plot(x, np.sinh(x), 'r-', linewidth=2)
ax2.set_title('$y = \\sinh x$')
ax2.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```
