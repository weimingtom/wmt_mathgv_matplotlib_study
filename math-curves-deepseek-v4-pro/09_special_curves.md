---
jupytext:
  text_representation:
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 9. 蝴蝶与特殊曲线 Special Curves

本意集合了蝴蝶曲线、超椭圆、以及其他独特的曲线。

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 120
plt.rcParams['axes.unicode_minus'] = False

def polar_to_xy(theta, r):
    return r * np.cos(theta), r * np.sin(theta)
```

## 9.1 蝴蝶曲线 Butterfly Curve

$r = e^{\cos t} - 2\cos(4t) + \sin^5(t/12)$

```{code-cell} ipython3
t = np.linspace(0, 12*np.pi, 4000)
r = np.exp(np.cos(t)) - 2*np.cos(4*t) + np.sin(t/12)**5
x, y = polar_to_xy(t, r)
fig, ax = plt.subplots(figsize=(8,8))
ax.plot(x, y, 'purple', linewidth=1)
ax.set_aspect('equal')
ax.set_title('Butterfly Curve / 蝴蝶曲线')
ax.grid(True, alpha=0.3)
plt.show()
```

## 9.2 蝴蝶曲线 参数形式

$x = \sin t \left(e^{\cos t} - 2\cos 4t\right)$

$y = \cos t \left(e^{\cos t} - 2\cos 4t\right)$

```{code-cell} ipython3
t = np.linspace(0, 12*np.pi, 4000)
factor = np.exp(np.cos(t)) - 2*np.cos(4*t)
x = np.sin(t) * factor
y = np.cos(t) * factor
fig, ax = plt.subplots(figsize=(8,8))
ax.plot(x, y, 'darkred', linewidth=1)
ax.set_aspect('equal')
ax.set_title('Butterfly Curve (Parametric Form)')
ax.grid(True, alpha=0.3)
plt.show()
```

## 9.3 超椭圆 Superellipse (Lamé Curve)

$|x/a|^r + |y/b|^r = 1$

当 $r=2$ 时为椭圆，$r$ 增大趋向矩形。

```{code-cell} ipython3
theta = np.linspace(0, 2*np.pi, 3000)
a, b = 1, 1
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
for r, ax in zip([0.5, 1.5, 2.0, 4.0], axes.flat):
    x = a * np.sign(np.cos(theta)) * np.abs(np.cos(theta))**(2/r)
    y = b * np.sign(np.sin(theta)) * np.abs(np.sin(theta))**(2/r)
    ax.plot(x, y, linewidth=2)
    ax.fill(x, y, alpha=0.15)
    ax.set_aspect('equal')
    ax.set_title(f'Superellipse r={r}')
    ax.grid(True, alpha=0.3)
plt.suptitle('Superellipse / 超椭圆', fontsize=14)
plt.tight_layout()
plt.show()
```

## 9.4 PIET HEIN 超椭圆 (Squircle)

$r=4$ 的特殊超椭圆 — 圆与方之间的形状。

```{code-cell} ipython3
r_param = 4
x = np.sign(np.cos(theta)) * np.abs(np.cos(theta))**(2/r_param)
y = np.sign(np.sin(theta)) * np.abs(np.sin(theta))**(2/r_param)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'blue', linewidth=2)
ax.fill(x, y, alpha=0.2, color='blue')
ax.set_aspect('equal')
ax.set_title('Squircle ($r=4$) / Piet Hein超级椭圆')
ax.grid(True, alpha=0.3)
plt.show()
```

## 9.5 双叶线 / 双扭线

$r = a\cos^2\theta$ 产生双叶图案

```{code-cell} ipython3
theta = np.linspace(0, 2*np.pi, 3000)
a = 2
r = a * np.cos(theta)**2
x, y = polar_to_xy(theta, r)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'darkgreen', linewidth=2)
ax.set_aspect('equal')
ax.set_title('Bifolium / 双叶线: $r = 2\\cos^2\\theta$')
ax.grid(True, alpha=0.3)
plt.show()
```

## 9.6 三叶线 Trifolium

$r = a\cos\theta\cos(3\theta)$

```{code-cell} ipython3
theta = np.linspace(0, 2*np.pi, 3000)
a = 2
r = a * np.cos(theta) * np.cos(3*theta)
x, y = polar_to_xy(theta, r)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'orange', linewidth=2)
ax.set_aspect('equal')
ax.set_title('Trifolium / 三叶线')
ax.grid(True, alpha=0.3)
plt.show()
```

## 9.7 星形线变体

不同参数的星形曲线。

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 2000)
fig, axes = plt.subplots(1, 3, figsize=(15,5))
for ax, n in zip(axes, [2, 3, 4]):
    x = np.cos(t)**n
    y = np.sin(t)**n
    ax.plot(x, y, linewidth=2)
    ax.set_aspect('equal')
    ax.set_title(f'$x=\\cos^{n}t, y=\\sin^{n}t$')
    ax.grid(True, alpha=0.3)
plt.suptitle('Astroid Variants', fontsize=14)
plt.tight_layout()
plt.show()
```

## 9.8 齿轮曲线 / 内齿轮曲线

来自 Hypotrochoid 的特殊参数。

```{code-cell} ipython3
t = np.linspace(0, 14*np.pi, 8000)
R, r, d = 7, 2, 5
x = (R-r)*np.cos(t) + d*np.cos((R-r)/r * t)
y = (R-r)*np.sin(t) - d*np.sin((R-r)/r * t)
fig, ax = plt.subplots(figsize=(7,7))
ax.plot(x, y, 'navy', linewidth=0.7)
ax.set_aspect('equal')
ax.set_title(f'Gear Curve R={R}, r={r}, d={d}')
ax.grid(True, alpha=0.2)
plt.show()
```

## 9.9 心形曲线 Heart Curve

$x = 16\sin^3 t, \quad y = 13\cos t - 5\cos 2t - 2\cos 3t - \cos 4t$

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 3000)
x = 16 * np.sin(t)**3
y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)
fig, ax = plt.subplots(figsize=(8,8))
ax.plot(x, y, 'red', linewidth=2)
ax.fill(x, y, alpha=0.3, color='red')
ax.set_aspect('equal')
ax.set_title('Heart Curve / 爱心曲线')
ax.grid(True, alpha=0.3)
plt.show()
```

## 9.10 梨形曲线 Pear Curve

$b^2y^2 = x^3(a-x)$

```{code-cell} ipython3
a, b = 3, 2
x = np.linspace(0, a, 2000)
y = np.sqrt(np.maximum(x**3*(a-x)/b**2, 0))
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(x, y, 'green', linewidth=2, label='Pear Curve')
ax.plot(x, -y, 'green', linewidth=2)
ax.fill_between(x, y, alpha=0.15, color='green')
ax.set_aspect('equal')
ax.set_title('Pear Curve / 梨形曲线')
ax.legend(); ax.grid(True, alpha=0.3)
plt.show()
```

## 9.11 子弹曲线 / 弹头曲线 Bullet Nose

$y = \\frac{a}{b^2 + x^2}$ 产生弹头形状。

```{code-cell} ipython3
x = np.linspace(-4, 4, 2000)
a, b = 4, 2
y = a / (b**2 + x**2)
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, y, 'darkblue', linewidth=2)
ax.fill_between(x, y, alpha=0.2, color='darkblue')
ax.set_title('Bullet Nose Curve / 弹头曲线')
ax.grid(True, alpha=0.3)
ax.set_ylim(0, 2.5)
plt.show()
```

## 9.12 鱼形曲线 Fish Curve

```{code-cell} ipython3
t = np.linspace(0, 2*np.pi, 3000)
x = np.cos(t) - np.sin(t)**2 / np.sqrt(2)
y = np.sin(t) * np.cos(t)
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(x, y, 'teal', linewidth=2)
ax.set_aspect('equal')
ax.set_title('Fish Curve / 鱼形曲线')
ax.grid(True, alpha=0.3)
plt.show()
```
