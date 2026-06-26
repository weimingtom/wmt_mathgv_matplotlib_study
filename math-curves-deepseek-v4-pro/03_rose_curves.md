---
jupytext:
  text_representation:
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 3. 玫瑰线 Rose Curves

极坐标方程 $r = a\cos(n\theta)$ 或 $r = a\sin(n\theta)$ 产生花瓣状曲线。$n$ 为整数时产生 $n$（奇数）或 $2n$（偶数）个花瓣。

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 120
plt.rcParams['axes.unicode_minus'] = False
```

## 3.1 二叶玫瑰线（n=1）

$r = \cos\theta$ — 形似圆

```{code-cell} ipython3
theta = np.linspace(0, 2*np.pi, 2000)
r = np.cos(theta)
x, y = r*np.cos(theta), r*np.sin(theta)
fig, ax = plt.subplots(figsize=(6,6))
ax.plot(x, y, linewidth=2)
ax.set_aspect('equal'); ax.set_title('Rose n=1: $r=\\cos\\theta$'); ax.grid(True, alpha=0.3)
plt.show()
```

## 3.2 三叶玫瑰线（n=3）

$r = \cos(3\theta)$ — 3个花瓣

```{code-cell} ipython3
n = 3
r = np.cos(n * theta)
x, y = r*np.cos(theta), r*np.sin(theta)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'b-', linewidth=2)
ax.fill(x, y, alpha=0.3, color='blue')
ax.set_aspect('equal'); ax.set_title(f'Rose n={n}: $r=\\cos({n}\\theta)$ — 3 petals')
ax.grid(True, alpha=0.3)
plt.show()
```

## 3.3 四叶玫瑰线（n=2）

$r = \cos(2\theta)$ — 4个花瓣

```{code-cell} ipython3
n = 2
r = np.cos(n * theta)
x, y = r*np.cos(theta), r*np.sin(theta)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'g-', linewidth=2)
ax.fill(x, y, alpha=0.3, color='green')
ax.set_aspect('equal'); ax.set_title(f'Rose n={n}: $r=\\cos({n}\\theta)$ — 4 petals')
ax.grid(True, alpha=0.3)
plt.show()
```

## 3.4 多叶玫瑰线 面板

$n = 1, 2, 3, 4, 5, 6, 7, 8$

```{code-cell} ipython3
fig, axes = plt.subplots(2, 4, figsize=(16, 9))
for idx, n in enumerate([1, 2, 3, 4, 5, 6, 7, 8]):
    ax = axes[idx//4][idx%4]
    r = np.cos(n * theta)
    x, y = r*np.cos(theta), r*np.sin(theta)
    petals = n if n % 2 == 1 else 2*n
    ax.plot(x, y, linewidth=1.5)
    ax.set_aspect('equal')
    ax.set_title(f'n={n} ({petals} petals)')
    ax.grid(True, alpha=0.2)
plt.suptitle('Rose Curves / 玫瑰线', fontsize=16)
plt.tight_layout()
plt.show()
```

## 3.5 玫瑰线 sin 版本

$r = \sin(n\theta)$ — 与 $\cos$ 版本旋转角度不同。

```{code-cell} ipython3
fig, axes = plt.subplots(2, 4, figsize=(16, 9))
for idx, n in enumerate([1, 2, 3, 4, 5, 6, 7, 8]):
    ax = axes[idx//4][idx%4]
    r = np.sin(n * theta)
    x, y = r*np.cos(theta), r*np.sin(theta)
    m = np.abs(r)  # 取绝对值
    x2, y2 = m*np.cos(theta), m*np.sin(theta)
    ax.plot(x2, y2, linewidth=1.5, color='red')
    ax.set_aspect('equal')
    ax.set_title(f'$r=|\\sin({n}\\theta)|$')
    ax.grid(True, alpha=0.2)
plt.suptitle('Rose Curves (sin, absolute value)', fontsize=16)
plt.tight_layout()
plt.show()
```

## 3.6 四叶玫瑰线 Rhodonea

$r = 5\sin(2\theta)$ — 经典四叶玫瑰线

```{code-cell} ipython3
r = 5 * np.sin(2 * theta)
x, y = r*np.cos(theta), r*np.sin(theta)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'darkred', linewidth=2)
ax.set_aspect('equal')
ax.set_title('Rhodonea: $r = 5\\sin(2\\theta)$')
ax.grid(True, alpha=0.3)
plt.show()
```

## 3.7 分数阶玫瑰线 $n = 1/2$

$r = \cos(\theta/2)$ — 产生特殊形状

```{code-cell} ipython3
theta_long = np.linspace(0, 4*np.pi, 4000)
n_half = 0.5
r = np.cos(n_half * theta_long)
x, y = r*np.cos(theta_long), r*np.sin(theta_long)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'purple', linewidth=1.5)
ax.set_aspect('equal')
ax.set_title('Fractional Rose: $r = \\cos(\\theta/2)$')
ax.grid(True, alpha=0.3)
plt.show()
```

## 3.8 玫瑰线 $n = 3/2$

```{code-cell} ipython3
theta_long = np.linspace(0, 4*np.pi, 4000)
n_f = 1.5
r = np.cos(n_f * theta_long)
x, y = r*np.cos(theta_long), r*np.sin(theta_long)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'teal', linewidth=1.5)
ax.set_aspect('equal')
ax.set_title('Fractional Rose: $r = \\cos(1.5\\,\\theta)$')
ax.grid(True, alpha=0.3)
plt.show()
```

## 3.9 玫瑰线 $n = 5/2$

```{code-cell} ipython3
n_f = 2.5
r = np.cos(n_f * theta_long)
x, y = r*np.cos(theta_long), r*np.sin(theta_long)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'orange', linewidth=1.5)
ax.set_aspect('equal')
ax.set_title('Fractional Rose: $r = \\cos(2.5\\,\\theta)$')
ax.grid(True, alpha=0.3)
plt.show()
```

## 3.10 玫瑰线 $n = 7/3$

```{code-cell} ipython3
theta_xtra = np.linspace(0, 6*np.pi, 6000)
n_f = 7/3
r = np.cos(n_f * theta_xtra)
x, y = r*np.cos(theta_xtra), r*np.sin(theta_xtra)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'brown', linewidth=1.5)
ax.set_aspect('equal')
ax.set_title('Fractional Rose: $r = \\cos(7\\theta/3)$')
ax.grid(True, alpha=0.3)
plt.show()
```
