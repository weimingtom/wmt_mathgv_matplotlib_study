---
jupytext:
  text_representation:
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# 数学曲线大全 · Mathematical Curves Collection

本项目使用 Matplotlib 和 Jupyter Notebook 绘制了 **120+ 条经典数学曲线**，涵盖几乎所有已知的平面曲线家族。每条曲线均配有中英文名称、数学方程，以及高质量的 Python 绘图代码。

---

## 曲线家族一览

| 章节 | 曲线族 | 数量 | 代表曲线 |
|------|--------|------|----------|
| 1 | 圆锥曲线 | 7 | 圆、椭圆、抛物线、双曲线 |
| 2 | 心形线与蚶线 | 10 | 心脏线、利马松、蚶线 |
| 3 | 玫瑰线 | 10 | 四叶玫瑰、多叶玫瑰 |
| 4 | 摆线族 | 12 | 摆线、外摆线、内摆线、星形线 |
| 5 | 螺旋线 | 12 | 阿基米德螺旋、对数螺旋、欧拉螺旋 |
| 6 | 李萨如曲线 | 10 | 各种频率比谐振曲线 |
| 7 | 代数曲线 | 14 | 双纽线、蔓叶线、笛卡尔叶形线 |
| 8 | 悬链与追踪 | 6 | 悬链线、追踪曲线、弹性曲线 |
| 9 | 特殊曲线 | 12 | 蝴蝶曲线、超椭圆、双叶线 |
| 10 | 经典函数 | 12 | 三角函数、正态分布、贝塞尔 |
| 11 | 卵形线 | 10 | 卡西尼卵形线、笛卡尔卵形线 |
| 12 | 杂项参数曲线 | 10 | 蜗牛线、梨形线等 |

---

## 使用说明

1. 安装依赖：`pip install numpy matplotlib scipy jupyter-book`
2. 逐个运行 notebook 查看曲线，或直接执行所有 cell
3. 构建 Jupyter Book：`jupyter-book build .`
4. 生成的 HTML 在 `_build/html/` 目录下

## 致谢

参考来源：
- Wikipedia - List of curves
- MathWorld (Wolfram)
- Desmos Graphing Calculator
- MathGV
- 本项目原始仓库的各独立 notebook
