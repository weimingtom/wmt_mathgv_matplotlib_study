---
jupytext:
  text_representation:
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 2. 心形线与蚶线 Cardioid & Limaçon

心形线是外摆线的一种，蚶线（利马松）是心形线的推广。这类曲线以极坐标方程 $r = a + b\cos\theta$ 定义。

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 120
plt.rcParams['axes.unicode_minus'] = False
theta = np.linspace(0, 2*np.pi, 2000)
```

## 2.1 心脏线（1-cosθ）Cardioid

$r = 1 - \cos\theta$

```{code-cell} ipython3
r = 1 - np.cos(theta)
x, y = r * np.cos(theta), r * np.sin(theta)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'r-', linewidth=2)
ax.fill(x, y, alpha=0.3, color='red')
ax.set_aspect('equal')
ax.set_title('Cardioid: $r = 1 - \\cos\\theta$')
ax.grid(True, alpha=0.3)
plt.show()
```

## 2.2 心脏线（1-sinθ）Cardioid

$r = 1 - \sin\theta$

```{code-cell} ipython3
r = 1 - np.sin(theta)
x, y = r * np.cos(theta), r * np.sin(theta)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'b-', linewidth=2)
ax.fill(x, y, alpha=0.3, color='blue')
ax.set_aspect('equal')
ax.set_title('Cardioid: $r = 1 - \\sin\\theta$')
ax.grid(True, alpha=0.3)
plt.show()
```

## 2.3 心脏线 参数方程 Cardioid Parametric

$x = a(2\cos t - \cos 2t), \quad y = a(2\sin t - \sin 2t)$

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 2000)
a = 0.5
x = a * (2*np.cos(t) - np.cos(2*t))
y = a * (2*np.sin(t) - np.sin(2*t))
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'r-', linewidth=2)
ax.fill(x, y, alpha=0.3, color='red')
ax.set_aspect('equal')
ax.set_title('Cardioid (Parametric)')
ax.grid(True, alpha=0.3)
plt.show()
```

## 2.4 蚶线 / 利马松 Limaçon

$r = 1 + b\cos\theta$, 不同 $b$ 值展示不同形态。

```{code-cell} ipython3
fig, axes = plt.subplots(2, 3, figsize=(14,10))
for idx, b in enumerate([0.3, 0.5, 0.7, 1.0, 1.3, 1.6]):
    ax = axes[idx//3][idx%3]
    r = 1 + b * np.cos(theta)
    x, y = r * np.cos(theta), r * np.sin(theta)
    ax.plot(x, y, linewidth=2)
    ax.fill(x, y, alpha=0.2)
    ax.set_aspect('equal')
    ax.set_title(f'Limaçon: $r = 1 + {b}\\cos\\theta$')
    ax.grid(True, alpha=0.3)
plt.suptitle('Limaçon Family / 蚶线族', fontsize=14)
plt.tight_layout()
plt.show()
```

## 2.5 内蚶线 / 有凹蚶线 Dimpled Limaçon

$b=0.7$ 时出现凹陷。

```{code-cell} ipython3
b = 0.7
r = 1 + b * np.cos(theta)
x, y = r * np.cos(theta), r * np.sin(theta)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'purple', linewidth=2)
ax.fill(x, y, alpha=0.2, color='purple')
ax.set_aspect('equal')
ax.set_title(f'Dimpled Limaçon: $r = 1 + {b}\\cos\\theta$')
ax.grid(True, alpha=0.3)
plt.show()
```

## 2.6 内环蚶线 / 带环利马松 Looped Limaçon

$b > 1$ 时出现内环。

```{code-cell} ipython3
b = 1.6
r = 1 + b * np.cos(theta)
x, y = r * np.cos(theta), r * np.sin(theta)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'darkred', linewidth=2)
ax.set_aspect('equal')
ax.set_title(f'Looped Limaçon: $r = 1 + {b}\\cos\\theta$')
ax.grid(True, alpha=0.3)
plt.show()
```

## 2.7 蚶线 尼科米德斯蚌线 Conchoid of Nicomedes

$r = a\sec\theta + b$

```{code-cell} ipython3
t1 = np.linspace(-np.pi/2 + 0.1, np.pi/2 - 0.1, 500)
t2 = np.linspace(np.pi/2 + 0.1, 3*np.pi/2 - 0.1, 500)
a, b = 1.0, 0.5
for b_val, color, label in [(0.5, 'blue', 'b=0.5'), (1.5, 'green', 'b=1.5'), (2.0, 'red', 'b=2.0')]:
    r1 = a/np.cos(t1) + b_val
    r2 = a/np.cos(t2) + b_val
    x1, y1 = r1*np.cos(t1), r1*np.sin(t1)
    x2, y2 = r2*np.cos(t2), r2*np.sin(t2)
    fig, ax = plt.subplots(figsize=(7,5))
    ax.plot(x1, y1, color=color, linewidth=2, label=label)
    ax.plot(x2, y2, color=color, linewidth=2)
    ax.set_aspect('equal')
    ax.set_title(f'Conchoid of Nicomedes: $r = \\sec\\theta + {b_val}$')
    ax.set_xlim(-3, 5); ax.set_ylim(-4, 4)
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.show()
```

## 2.8 帕斯卡蚶线 Pascal's Limaçon

$r = b + 2a\cos\theta$ — 蚶线的另一种参数化。

```{code-cell} ipython3
for a_val in [0.3, 0.6, 1.0]:
    r = 1 + 2*a_val*np.cos(theta)
    x, y = r*np.cos(theta), r*np.sin(theta)
    fig, ax = plt.subplots(figsize=(6,6))
    ax.plot(x, y, linewidth=2)
    ax.fill(x, y, alpha=0.15)
    ax.set_aspect('equal')
    ax.set_title(f"Pascal's Limaçon: $r = 1 + {2*a_val}\\cos\\theta$")
    ax.grid(True, alpha=0.3)
    plt.show()
```

## 2.9 蜗线 / 蚶线变体

$r = a\cos\theta + b$ 的 sin 版本。

```{code-cell} ipython3
for b_val in [0.5, 1.0, 1.5]:
    r = 1 + b_val * np.sin(theta)
    x, y = r*np.cos(theta), r*np.sin(theta)
    fig, ax = plt.subplots(figsize=(6,6))
    ax.plot(x, y, linewidth=2)
    ax.fill(x, y, alpha=0.15, color='orange')
    ax.set_aspect('equal')
    ax.set_title(f'$r = 1 + {b_val}\\sin\\theta$')
    ax.grid(True, alpha=0.3)
    plt.show()
```

## 2.10 心形线对比 Cardioid Comparison

$r = 1 - \cos\theta$ vs $r = 1 - \sin\theta$

```{code-cell} ipython3
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))
r1 = 1 - np.cos(theta); x1, y1 = r1*np.cos(theta), r1*np.sin(theta)
r2 = 1 - np.sin(theta); x2, y2 = r2*np.cos(theta), r2*np.sin(theta)
ax1.plot(x1, y1, 'r-', linewidth=2); ax1.fill(x1, y1, alpha=0.3, color='red')
ax1.set_aspect('equal'); ax1.set_title('$r = 1 - \\cos\\theta$'); ax1.grid(True, alpha=0.3)
ax2.plot(x2, y2, 'b-', linewidth=2); ax2.fill(x2, y2, alpha=0.3, color='blue')
ax2.set_aspect('equal'); ax2.set_title('$r = 1 - \\sin\\theta$'); ax2.grid(True, alpha=0.3)
plt.suptitle('Cardioid: cos vs sin', fontsize=14)
plt.tight_layout()
plt.show()
```
