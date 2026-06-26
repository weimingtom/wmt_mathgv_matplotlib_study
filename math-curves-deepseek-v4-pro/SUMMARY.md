# 数学曲线大全 · Jupyter Book 总结

## 总体信息
- **曲线总数**：125 条
- **章节数**：12 章 + 1 篇导论
- **格式**：MyST Markdown (.md)，带 Jupyter Book 兼容的 Jupytext frontmatter
- **构建方法**：`jupyter-book build .` 在项目根目录执行

## 章节清单

| 文件 | 曲线数 | 内容 |
|------|--------|------|
| 00_intro.md | — | 总目录 / 简介 |
| 01_conic_sections.md | 7 | 圆、椭圆、抛物线、双曲线、退化圆锥 |
| 02_cardioid_limacon.md | 10 | 心脏线（cos/sin/参数形式）、利马松、尼科米德斯蚌线 |
| 03_rose_curves.md | 10 | 玫瑰线 n=1~8（整数阶）及分数阶 n=1/2, 3/2, 5/2, 7/3 |
| 04_cycloid_family.md | 12 | 摆线、外摆线、内摆线、星形线、三尖瓣线、肾形线、长短辐摆线/外摆线/内摆线（万花尺） |
| 05_spirals.md | 12 | 阿基米德螺旋、对数螺旋、费马螺旋、双曲螺旋、连锁螺线、欧拉螺旋/羊角螺线、科努螺旋、西奥多罗斯螺旋、斐波那契螺旋、黄金螺旋、伽利略螺旋、尼尔森螺旋 |
| 06_lissajous.md | 10 | 李萨如曲线（1:1~8:5 频率比）、相位变化、余弦版、混合 sin/cos 版、3D 投影 |
| 07_algebraic_curves.md | 14 | 伯努利双纽线、蔓叶线、阿涅西的女巫、笛卡尔叶形线、蛇形线、双扭线、立方抛物线、半立方抛物线、四次曲线、珍珠线、Trident、Bicorn、牛顿三叉线、双曲函数曲线 |
| 08_catenary_pursuit.md | 6 | 悬链线（变参数）、追踪曲线、弹性曲线、匀速追踪、拖曳曲线族 |
| 09_special_curves.md | 12 | 蝴蝶曲线（极坐标/参数）、超椭圆（含 Squircle）、双叶线、三叶线、星形线变体、齿轮曲线、爱心曲线、梨形曲线、弹头曲线、鱼形曲线 |
| 10_function_curves.md | 12 | 正弦/余弦/正切、指数函数、对数函数、正态分布/高斯、误差函数、Sinc 函数、Sigmoid、阻尼振荡、贝塞尔曲线、Beta 分布 |
| 11_ovals.md | 10 | 卡西尼卵形线（6 种参数）、笛卡尔卵形线（6 种参数）、Booth 卵形、四次卵形、蛋形曲线（3 种）、莫斯蛋、弹道卵形、美式足球曲线、仿卵线、卵形线对比面板 |
| 12_parametric_misc.md | 10 | 蜗牛线、螺形线、等角螺线、广义对数螺旋、谐波乘积、振荡圆周、螺线管曲线、谐波叠加、立方菱形、八角星 |

## 项目文件结构

```
wmt_mathgv_matplotlib_study-master/
├── _config.yml                    # Jupyter Book 配置
├── _toc.yml                       # 目录结构
├── 00_intro.md                    # 介绍页
├── 01_conic_sections.md           # 第一章
├── 02_cardioid_limacon.md         # 第二章
├── 03_rose_curves.md              # 第三章
├── 04_cycloid_family.md           # 第四章
├── 05_spirals.md                  # 第五章
├── 06_lissajous.md                # 第六章
├── 07_algebraic_curves.md         # 第七章
├── 08_catenary_pursuit.md         # 第八章
├── 09_special_curves.md           # 第九章
├── 10_function_curves.md          # 第十章
├── 11_ovals.md                    # 第十一章
├── 12_parametric_misc.md          # 第十二章
├── README.md                      # 原始项目说明
├── *.ipynb                        # 原始独立 notebook（保留）
└── vendor/                        # 参考资料
```

## 使用说明

### 构建 Jupyter Book
```bash
cd wmt_mathgv_matplotlib_study-master
pip install jupyter-book numpy matplotlib scipy
jupyter-book build .
```
生成的 HTML 在 `_build/html/` 目录下。

### 直接在 Jupyter 中运行
每个 .md 文件可通过 Jupytext 作为 notebook 打开：
```bash
jupyter notebook 01_conic_sections.md
```

### 参考来源
- Wikipedia - List of curves
- MathWorld (Wolfram)
- Desmos Graphing Calculator
- MathGV
- 本项目原始仓库的各独立 notebook（all_math_curves_gpt_5_5.ipynb, mathematical_curves_collection.ipynb 等）
