# wmt_mathgv_matplotlib_study
[WIP] My MathGV and Matplotlib study, just for fun  

## Softwares  
* http://www.mathgv.com
* https://matplotlib.org  
https://matplotlib.org/stable/gallery/index  
* https://www.desmos.com/calculator?lang=zh-CN
* https://www.bilibili.com/video/BV1b6RjBaECk/
* HP Prime Virtual Calculator, HP_Prime_Virtual_Calculator_x64_2025_09_15.exe   
https://updates.moravia-consulting.com    
https://hpcalcs.com/download/    
* HP Prime Graphics Utilities  
https://www.hpcalc.org/prime/graphics/  
* HP Prime Math Applications  
https://www.hpcalc.org/prime/math/  

## Astroid, Tetracuspid
* https://en.wikipedia.org/wiki/Astroid
* https://github.com/weimingtom/wmt_mathgv_matplotlib_study/blob/master/astroid.ipynb
```
星型线。星形线是内摆线的一种。
星形线（astroid）或称为四尖瓣线（tetracuspid），
是一个有四个尖点的内摆线，也属于超椭圆的一种。 ​​​
```
* desmos: (4*cos(t)^3,4*sin(t)^3), 0<=t<=2pi  
https://www.desmos.com/calculator/4hyj0xccub   
```
(4*\cos(t)^{3},4*\sin(t)^{3})
0
2\pi
```

## Cardioid
* https://en.wikipedia.org/wiki/Cardioid
* https://github.com/weimingtom/wmt_mathgv_matplotlib_study/blob/master/cardioid.ipynb
```
心脏线，也称心形线，是外摆线的一种，亦为蚶线的一种，
是一个圆上的固定一点在它绕着与其相切且半径相同的另外
一个圆周滚动时所形成的轨迹，因其形状像心形而得名
```
* desmos: r=1-sin(theta)     
https://www.desmos.com/calculator/yap3w53rfo    
```
r=1-\sin\left(\theta\right)
```
* desmos: r=1-cos(theta)    
https://www.desmos.com/calculator/nhiabbwuxe  
```
r=1-\cos\left(\theta\right)
```

## Rose, Rhodonea Curve
* https://en.wikipedia.org/wiki/Rose_(mathematics)
* https://github.com/weimingtom/wmt_mathgv_matplotlib_study/blob/master/rhodonea.ipynb  
```
四叶玫瑰线
四叶玫瑰线是数学中的一种曲线，因形似花瓣而得名
四叶玫瑰线可通过两个圆周运动叠加生成，利用齿轮装置可精确绘制该曲线。
工程中曾研究其蚌线特性，并应用于椭圆形零件切削加工方案的近似设计

用matplotlib和Jupyter画四叶玫瑰线，效果如图。值得一提的是matplotlib画极坐标会忽略掉负数，
所以画出来是只有两叶玫瑰线，可以加上绝对值来变成正确的四叶（可能还有其他方法，但暂时这样实现）
```
* desmos: r=5*sin(2*theta) ​  ​  
https://www.desmos.com/calculator/ohlxw71rgx    
```
​r=5*\sin\left(2*\theta\right)
```

## Claude Haiku 4.5 generated code  
* https://github.com/weimingtom/wmt_mathgv_matplotlib_study/blob/master/mathematical_curves_collection.ipynb

## GPT-5 mini generated code (not good, need to be modified by Claude Haiku 4.5)
* https://github.com/weimingtom/wmt_mathgv_matplotlib_study/blob/master/all_math_curves.ipynb

## GPT-5.5 generated code
* https://github.com/weimingtom/wmt_mathgv_matplotlib_study/blob/master/all_math_curves_gpt_5_5.ipynb

## Deepseek-v4-pro generated code
* https://github.com/weimingtom/wmt_mathgv_matplotlib_study/blob/master/math-curves-deepseek-v4-pro/01_conic_sections.ipynb
* https://github.com/weimingtom/wmt_mathgv_matplotlib_study/blob/master/math-curves-deepseek-v4-pro/02_cardioid_limacon.ipynb
* https://github.com/weimingtom/wmt_mathgv_matplotlib_study/blob/master/math-curves-deepseek-v4-pro/03_rose_curves.ipynb
* https://github.com/weimingtom/wmt_mathgv_matplotlib_study/blob/master/math-curves-deepseek-v4-pro/04_cycloid_family.ipynb
* https://github.com/weimingtom/wmt_mathgv_matplotlib_study/blob/master/math-curves-deepseek-v4-pro/05_spirals.ipynb
* https://github.com/weimingtom/wmt_mathgv_matplotlib_study/blob/master/math-curves-deepseek-v4-pro/06_lissajous.ipynb
* https://github.com/weimingtom/wmt_mathgv_matplotlib_study/blob/master/math-curves-deepseek-v4-pro/07_algebraic_curves.ipynb
* https://github.com/weimingtom/wmt_mathgv_matplotlib_study/blob/master/math-curves-deepseek-v4-pro/08_catenary_pursuit.ipynb
* https://github.com/weimingtom/wmt_mathgv_matplotlib_study/blob/master/math-curves-deepseek-v4-pro/09_special_curves.ipynb
* https://github.com/weimingtom/wmt_mathgv_matplotlib_study/blob/master/math-curves-deepseek-v4-pro/10_function_curves.ipynb
* https://github.com/weimingtom/wmt_mathgv_matplotlib_study/blob/master/math-curves-deepseek-v4-pro/11_ovals.ipynb
* https://github.com/weimingtom/wmt_mathgv_matplotlib_study/blob/master/math-curves-deepseek-v4-pro/12_parametric_misc.ipynb

## Old mathgv 3.1 record, 2004/1/4-2004/1/14, from a book, but I forget the book name  
* 蝴蝶线, Y=f(x)=sqrt(8x)+4*sqrt(1-x/8)
* 对数螺线, R=e^(0.1*theta), 0<=theta<=20pi
* 三叶玫瑰线, R=5*sin(3*Theta), 0<=theta<=2pi
* 六叶玫瑰线, R=5*sin(4*Theta), 0<=theta<=2pi
* 四叶玫瑰线, R=5*sin(2*Theta), 0<=theta<=2pi
* 环索线, R=4*(1-sin(Theta))/cos(Theta), 0<=theta<=2pi; R=4*(1+sin(Theta))/cos(Theta), 0<=theta<=2pi
* 贝努利双纽线, R=sqrt(2*4^2*cos(2*Theta)), 0<=theta<=2pi
* 卡帕曲线, R=5*cot(Theta), 0<=theta<=2pi
* 悬链线, Y=f(x)=3/2*(e^(x/3)+e^(-x/3))
* 翼琴线, Y=f(x)=sqrt(       (x - 0.05)^2    *   (2^2-x^2)   /   (x+2)^2      ); Y=f(x)=-sqrt(       (x - 0.05)^2    *   (2^2-x^2)   /   (x+2)^2      )
* 欧道克斯枕头线, Y=f(x)=sqrt( x^4/1^2-x^2   ); Y=f(x)=-sqrt( x^4/1^2-x^2   )
* 童衫线, Y=f(x)=sqrt(1*(x+1)^2/x); Y=f(x)=-sqrt(1*(x+1)^2/x)
* 8字线, Y=f(x)=sqrt (x^2-x^4/(4*2^2) ); Y=f(x)=- sqrt (x^2-x^4/(4*2^2) )
* 荷包线, Y=f(x)= -sqrt( 4*(2^2+2^2)*x^2/( 4*( 2*x+2^2) - 1) ); Y=f(x)=sqrt( 4*(2^2+2^2)*x^2/( 4*( 2*x+2^2) - 1) )
* 沙钟线, Y=f(x)=sqrt(  (4*2^4*x^2+10^2*2^2)/(10^2-4*2^2)  ); Y=f(x)=-sqrt(  (4*2^4*x^2+10^2*2^2)/(10^2-4*2^2)  )
* 史留斯珍珠线, Y=f(x)=  (7*x^3-x^4)^(1/4); Y=f(x)=  -    (7*x^3-x^4)^(1/4)
* 隆桑珍珠线, Y=f(x)=  (x^4-2*3*x^3)^(1/4); Y=f(x)= - (x^4-2*3*x^3)^(1/4)
* 斜环索线（布尔密斯特曲线）, R=1/cos(Theta)+1*tan(Theta)-2, 0<=theta<=2pi
* 滑绳线, Y=f(x)=sqrt(x^2*(1-x)^2/(2^2-x^2) ); Y=f(x)=-sqrt(x^2*(1-x)^2/(2^2-x^2) )
* 曳物线, X=5 *(ln(tan(T/2))+cos(T) ), Y=5 *sin(T), 0<=T<=2pi
* 三次抛物线, Y=f(x)=1*x^4-3*x^3-6*x^2+1*x+1
* 回旋曲线, X=T - 3^2*T^5/40, Y=3*T^3/6, 0<=T<=2pi
* 最速降线, X=1*(T-sin(T)), Y=1*(1-cos(T)), 0<=T<=2pi
* 短幅摆线, X=2*T-1*sin(T), Y=2   -1*cos(T), 0<=T<=2pi
* 内摆线, X=5*(  (1-0.8)*cos(0.8*T)+ 0.8*cos((1-0.8)*T)  ), Y=5*(  (1-0.8)*sin(0.8*T)  - 0.8*sin((1-0.8)*T)  ), 0<=T<=20pi
* 外摆线, X=1*(  (1+1)*cos(1*T)- 1*cos((1+1)*T)  )    , Y=1*(  (1+1)*sin(0.8*T)  - 1*sin((1+1)*T)  ), 0<=T<=2pi
* 星型线, X=4*cos(T)^3, Y=4*sin(T)^3, 0<=T<=2pi
* 心脏线，R=2*1*(1-cos(Theta)), 0<=Theta<=2pi
* 第一蜗线, R=2*1*cos(Theta)+1, 0<=Theta<=2pi
* 第三蜗线, R=2*1*cos(Theta)+2.3, 0<=Theta<=2pi
* 长幅内摆线, X=1*(  (1-0.8)*cos(0.8*T)+ 2*cos((1-0.8)*T)  ), Y=1*(  (1-0.8)*sin(0.8*T)  - 2*sin((1-0.8)*T)  ), 0<=T<=20pi
* 短幅内摆线, X=3*(  (1-0.8)*cos(0.8*T)+ 0.5*cos((1-0.8)*T)  ), Y=3*(  (1-0.8)*sin(0.8*T)  - 0.5*sin((1-0.8)*T)  ), 0<=T<=20pi
* 无穷多叶玫瑰线, R=5*sin( sqrt(5) *Theta), 0<=Theta<=10pi
* 分割正五边形, X=1*cos((3/5)*T)+0.3*cos(  (1-(3/5)) *T), Y=1*sin((3/5)*T)  - 0.3*sin(  (1-(3/5)) *T), 0<=Theta<=10pi
* 分割正六边形, X=1*cos((1/6)*T)+0.3*cos(  (1-(1/6)) *T), Y=1*sin((1/6)*T)  - 0.3*sin(  (1-(1/6)) *T), 0<=Theta<=20pi
* 分割正三角形, X=1*cos((1/3)*T)+0.3*cos(  (1-(1/3)) *T), Y=1*sin((1/3)*T)  - 0.3*sin(  (1-(1/3)) *T), 0<=Theta<=20pi
* 分割正七边形, X=1*cos((3/7)*T)+0.3*cos(  (1-(3/7)) *T), Y=1*sin((3/7)*T)  - 0.3*sin(  (1-(3/7)) *T), 0<=Theta<=20pi
* 笛卡儿叶形线, X=3*2*T/(1+T^3), Y=3*2*T^2/(1+T^3), 0<=Theta<=20pi
* 长幅摆线, X=1*T-2*sin(T) , Y=1   -2*cos(T), 0<=Theta<=20pi
* 短幅外摆线, X=1*(  (1+1)*cos(1*T)- 0.5*cos((1+1)*T)  )    , Y=1*(  (1+1)*sin(0.8*T)  - 0.5*sin((1+1)*T)  ), 0<=Theta<=10pi

