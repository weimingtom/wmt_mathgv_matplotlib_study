---
jupytext:
  text_representation:
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 4. 摆线族 Cycloid Family

当一个圆沿直线或另一个圆滚动时，圆上一点画出的轨迹。

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 120
plt.rcParams['axes.unicode_minus'] = False
```

## 4.1 摆线 Cycloid

$x = r(t - \sin t), \quad y = r(1 - \cos t)$

```{code-cell} ipython3
t = np.linspace(0, 6*np.pi, 3000)
r = 1
x = r * (t - np.sin(t))
y = r * (1 - np.cos(t))
fig, ax = plt.subplots(figsize=(14, 5))
ax.plot(x, y, 'b-', linewidth=2)
ax.set_aspect('equal'); ax.set_title('Cycloid / 摆线')
ax.grid(True, alpha=0.3); plt.show()
```

## 4.2 外摆线 Epicycloid

圆在另一个圆外侧滚动。

$x = (R+r)\cos t - r\cos\left(\frac{R+r}{r}t\right), \quad y = (R+r)\sin t - r\sin\left(\frac{R+r}{r}t\right)$

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 3000)
fig, axes = plt.subplots(1, 3, figsize=(15,5))
for idx, (R, rr) in enumerate([(5,1), (4,1), (3,1)]):
    ax = axes[idx]
    x = (R+rr)*np.cos(t) - rr*np.cos((R+rr)/rr * t)
    y = (R+rr)*np.sin(t) - rr*np.sin((R+rr)/rr * t)
    ax.plot(x, y, linewidth=2)
    ax.set_aspect('equal')
    ax.set_title(f'Epicycloid R={R}, r={rr} ({R} cusps)')
    ax.grid(True, alpha=0.3)
plt.suptitle('Epicycloid / 外摆线', fontsize=14)
plt.tight_layout(); plt.show()
```

## 4.3 内摆线 Hypocycloid

圆在另一个圆内侧滚动。

$x = (R-r)\cos t + r\cos\left(\frac{R-r}{r}t\right), \quad y = (R-r)\sin t - r\sin\left(\frac{R-r}{r}t\right)$

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 3000)
fig, axes = plt.subplots(1, 3, figsize=(15,5))
for idx, (R, rr) in enumerate([(5,1), (4,1), (3,1)]):
    ax = axes[idx]
    x = (R-rr)*np.cos(t) + rr*np.cos((R-rr)/rr * t)
    y = (R-rr)*np.sin(t) - rr*np.sin((R-rr)/rr * t)
    ax.plot(x, y, linewidth=2)
    ax.set_aspect('equal')
    ax.set_title(f'Hypocycloid R={R}, r={rr} ({R} cusps)')
    ax.grid(True, alpha=0.3)
plt.suptitle('Hypocycloid / 内摆线', fontsize=14)
plt.tight_layout(); plt.show()
```

## 4.4 星形线 Astroid (Hypocycloid R=4, r=1)

$x = a\cos^3 t, \quad y = a\sin^3 t$

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 2000)
a = 4
x = a * np.cos(t)**3
y = a * np.sin(t)**3
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'c-', linewidth=2)
ax.fill(x, y, alpha=0.3, color='cyan')
ax.set_aspect('equal')
ax.set_title('Astroid / 星形线: $x=4\\cos^3t, y=4\\sin^3t$')
ax.grid(True, alpha=0.3); plt.show()
```

## 4.5 三尖瓣线 Deltoid (R=3, r=1)

内摆线 R=3, r=1 产生三个尖点。

```{code-cell} ipython3
R, rr = 3, 1
x = (R-rr)*np.cos(t) + rr*np.cos((R-rr)/rr * t)
y = (R-rr)*np.sin(t) - rr*np.sin((R-rr)/rr * t)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'r-', linewidth=2)
ax.set_aspect('equal')
ax.set_title('Deltoid / 三尖瓣线')
ax.grid(True, alpha=0.3); plt.show()
```

## 4.6 肾形线 Nephroid (Epicycloid R=2, r=1)

外摆线 R=2, r=1 — 形似肾脏。

```{code-cell} ipython3
R, rr = 2, 1
x = (R+rr)*np.cos(t) - rr*np.cos((R+rr)/rr * t)
y = (R+rr)*np.sin(t) - rr*np.sin((R+rr)/rr * t)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'g-', linewidth=2)
ax.set_aspect('equal')
ax.set_title('Nephroid / 肾形线')
ax.grid(True, alpha=0.3); plt.show()
```

## 4.7 长短辐摆线 Trochoid

圆滚动时非边缘点的轨迹（在圆内/外）。

```{code-cell} ipython3
t = np.linspace(0, 6*np.pi, 3000)
R, d = 1, 0.5  # d < 1: 短辐摆线
x = R*t - d*np.sin(t)
y = R - d*np.cos(t)
fig, ax = plt.subplots(figsize=(14, 4))
ax.plot(x, y, linewidth=1.5)
ax.set_aspect('equal')
ax.set_title(f'Trochoid (d={d}) / 短辐摆线')
ax.grid(True, alpha=0.3); plt.show()
```

## 4.8 长短辐外摆线 Epitrochoid

```{code-cell} ipython3
t = np.linspace(0, 4*np.pi, 3000)
R, r, d = 3, 1, 1.5
x = (R+r)*np.cos(t) - d*np.cos((R+r)/r * t)
y = (R+r)*np.sin(t) - d*np.sin((R+r)/r * t)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'purple', linewidth=1.5)
ax.set_aspect('equal')
ax.set_title(f'Epitrochoid (R={R}, r={r}, d={d})')
ax.grid(True, alpha=0.3); plt.show()
```

## 4.9 长短辐内摆线 Hypotrochoid

万花尺 Spirograph 画出的就是 Hypotrochoid。

```{code-cell} ipython3
t = np.linspace(0, 10*np.pi, 5000)
R, r, d = 5, 3, 2.5
x = (R-r)*np.cos(t) + d*np.cos((R-r)/r * t)
y = (R-r)*np.sin(t) - d*np.sin((R-r)/r * t)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'darkblue', linewidth=1)
ax.set_aspect('equal')
ax.set_title(f'Hypotrochoid / Spirograph (R={R}, r={r}, d={d})')
ax.grid(True, alpha=0.3); plt.show()
```

## 4.10 万花尺变体 Spirograph Variants

不同参数产生各种精美图案。

```{code-cell} ipython3
t = np.linspace(0, 12*np.pi, 8000)
fig, axes = plt.subplots(2, 2, figsize=(12,12))
params = [(5,2,4), (7,3,5), (9,4,6), (11,5,8)]
for (R,r,d), ax in zip(params, axes.flat):
    x = (R-r)*np.cos(t) + d*np.cos((R-r)/r * t)
    y = (R-r)*np.sin(t) - d*np.sin((R-r)/r * t)
    ax.plot(x, y, linewidth=0.7)
    ax.set_aspect('equal')
    ax.set_title(f'Spirograph R={R}, r={r}, d={d}')
    ax.grid(True, alpha=0.2)
plt.suptitle('Hypotrochoid / Spirograph Variations', fontsize=14)
plt.tight_layout(); plt.show()
```

## 4.11 摆线变体 Rolling Circle

多个周期的摆线比较。

```{code-cell} ipython3
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14,5))
t_short = np.linspace(0, 2*np.pi, 2000)
x1 = t_short - np.sin(t_short); y1 = 1 - np.cos(t_short)
ax1.plot(x1, y1, linewidth=2)
ax1.set_aspect('equal'); ax1.set_title('Cycloid — 1 cycle')
ax1.grid(True, alpha=0.3)
t_long = np.linspace(0, 10*np.pi, 5000)
x2 = t_long - np.sin(t_long); y2 = 1 - np.cos(t_long)
ax2.plot(x2, y2, 'r-', linewidth=1.5)
ax2.set_aspect('equal'); ax2.set_title('Cycloid — 5 cycles')
ax2.grid(True, alpha=0.3)
plt.tight_layout(); plt.show()
```

## 4.12 双摆线 — 两圆叠加

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 3000)
R1, r1 = 3, 1
R2, r2 = 7, 2
x1 = (R1-r1)*np.cos(t) + r1*np.cos((R1-r1)/r1*t)
y1 = (R1-r1)*np.sin(t) - r1*np.sin((R1-r1)/r1*t)
x2 = (R2-r2)*np.cos(t) + r2*np.cos((R2-r2)/r2*t)
y2 = (R2-r2)*np.sin(t) - r2*np.sin((R2-r2)/r2*t)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))
ax1.plot(x1, y1, linewidth=2); ax1.set_aspect('equal')
ax1.set_title('Hypocycloid R=3, r=1 (Deltoid)'); ax1.grid(True, alpha=0.3)
ax2.plot(x2, y2, 'g-', linewidth=2); ax2.set_aspect('equal')
ax2.set_title('Hypocycloid R=7, r=2 (7/2 lobes)'); ax2.grid(True, alpha=0.3)
plt.tight_layout(); plt.show()
```
