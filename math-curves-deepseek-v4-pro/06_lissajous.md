---
jupytext:
  text_representation:
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 6. 李萨如曲线 Lissajous Curves

两个相互垂直的简谐振动叠加形成的曲线：

$x = A\sin(at + \delta), \quad y = B\sin(bt)$

当频率比 $a:b$ 为有理数时曲线闭合。

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 120
plt.rcParams['axes.unicode_minus'] = False
```

## 6.1 1:1 同频 Lissajous

相位差产生圆、椭圆、线段。

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 2000)
fig, axes = plt.subplots(2, 3, figsize=(14, 9))
for idx, delta in enumerate([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 5*np.pi/4]):
    ax = axes[idx//3][idx%3]
    x = np.sin(t + delta)
    y = np.sin(t)
    ax.plot(x, y, linewidth=2)
    ax.set_aspect('equal')
    ax.set_title(f'1:1, delta={delta:.2f}')
    ax.grid(True, alpha=0.3)
plt.suptitle('Lissajous 1:1 with varying phase', fontsize=14)
plt.tight_layout()
plt.show()
```

## 6.2 3:2 Lissajous

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 2000)
x = np.sin(3*t)
y = np.sin(2*t)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'b-', linewidth=2)
ax.set_aspect('equal')
ax.set_title('Lissajous 3:2')
ax.grid(True, alpha=0.3)
plt.show()
```

## 6.3 5:4 Lissajous

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 3000)
x = np.sin(5*t)
y = np.sin(4*t)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'g-', linewidth=2)
ax.set_aspect('equal')
ax.set_title('Lissajous 5:4')
ax.grid(True, alpha=0.3)
plt.show()
```

## 6.4 5:3 Lissajous

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 3000)
x = np.sin(5*t)
y = np.sin(3*t)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'r-', linewidth=2)
ax.set_aspect('equal')
ax.set_title('Lissajous 5:3')
ax.grid(True, alpha=0.3)
plt.show()
```

## 6.5 7:5 Lissajous

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 3000)
x = np.sin(7*t)
y = np.sin(5*t)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'purple', linewidth=2)
ax.set_aspect('equal')
ax.set_title('Lissajous 7:5')
ax.grid(True, alpha=0.3)
plt.show()
```

## 6.6 多频率组合面板

不同频率比产生不同图案。

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 3000)
ratios = [(2,1), (3,2), (4,3), (5,4), (5,3), (7,5), (7,4), (8,5)]
fig, axes = plt.subplots(2, 4, figsize=(16, 9))
for idx, (a, b) in enumerate(ratios):
    ax = axes[idx//4][idx%4]
    x = np.sin(a*t)
    y = np.sin(b*t)
    ax.plot(x, y, linewidth=1.5)
    ax.set_aspect('equal')
    ax.set_title(f'{a}:{b}')
    ax.grid(True, alpha=0.2)
plt.suptitle('Lissajous Frequency Ratios / 李萨如曲线', fontsize=16)
plt.tight_layout()
plt.show()
```

## 6.7 相位差变化 Lissajous Phase

3:2 比例下不同相位差的影响。

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 3000)
fig, axes = plt.subplots(2, 3, figsize=(14, 9))
for idx, delta in enumerate([0, np.pi/6, np.pi/3, np.pi/2, 2*np.pi/3, 5*np.pi/6]):
    ax = axes[idx//3][idx%3]
    x = np.sin(3*t + delta)
    y = np.sin(2*t)
    ax.plot(x, y, linewidth=1.5)
    ax.set_aspect('equal')
    ax.set_title(f'3:2, delta={delta/np.pi:.2f}\\pi')
    ax.grid(True, alpha=0.3)
plt.suptitle('Lissajous 3:2 — Phase Variation', fontsize=14)
plt.tight_layout()
plt.show()
```

## 6.8 余弦版本 Lissajous (cos)

用 $\cos$ 替代 $\sin$ 产生旋转。

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 3000)
ratios = [(2,1), (3,2), (5,4), (7,5)]
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
for (a, b), ax in zip(ratios, axes.flat):
    x = np.cos(a*t)
    y = np.cos(b*t)
    ax.plot(x, y, 'darkred', linewidth=1.5)
    ax.set_aspect('equal')
    ax.set_title(f'cos {a}:{b}')
    ax.grid(True, alpha=0.3)
plt.suptitle('Lissajous (cos version)', fontsize=14)
plt.tight_layout()
plt.show()
```

## 6.9 混合版本 sin/cos

$x = \sin(at), y = \cos(bt)$

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 3000)
ratios = [(2,1), (3,2), (5,3), (7,4)]
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
for (a, b), ax in zip(ratios, axes.flat):
    x = np.sin(a*t)
    y = np.cos(b*t)
    ax.plot(x, y, 'teal', linewidth=1.5)
    ax.set_aspect('equal')
    ax.set_title(f'sin{int(a)}t, cos{int(b)}t')
    ax.grid(True, alpha=0.3)
plt.suptitle('Lissajous (mixed sin/cos)', fontsize=14)
plt.tight_layout()
plt.show()
```

## 6.10 3D 投影效果

Lissajous 在 3D 空间中的投影。

```{code-cell} ipython3
t = np.linspace(0, 4*np.pi, 4000)
a, b = 5, 4
x = np.sin(a*t)
y = np.sin(b*t)
fig, ax = plt.subplots(figsize=(8,8))
for z_scale in np.linspace(0, 1, 8):
    z = z_scale * np.cos(3*t)
    ax.plot(x + z*0.3, y + z*0.3, alpha=0.3+0.7*z_scale, linewidth=1)
ax.set_aspect('equal')
ax.set_title('Lissajous with quasi-3D offset')
ax.grid(True, alpha=0.3)
plt.show()
```
