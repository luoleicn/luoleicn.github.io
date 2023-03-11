#两点之间直线最短的证明



两点之间直线最短是非常符合人的直觉的，但在欧氏几何中两点之间直线最短并不是以公理形式存在的，也就是说是需要证明的，本文就讨论如何证明这一点。

![image](http://www.luolei.site/source/images/line.png)

求经过(a, \\(\alpha\\))和(b, \\(\beta\\))最短的曲线，这里只考虑平滑曲线\\(y=u(x)\\)，根据微积分和极限的基本原理，可以把曲线切分成非常短的片段，在非常短的范围里\\(\delta x \to 0\\)，可以把曲线理解为直角三角形的斜边，则曲线长度\\(s = \sqrt{ (\delta x)^2 + (\delta y)^2}\\)，所以曲线距离公式为：


\\[   
J(u) = \int_{a}^{b}\sqrt{1 + u^{'}(x)^2}dx 
\\]

\\[   
s.t. \quad u(a) = \alpha,\quad u(b) = \beta
\\]


为了表示方便令\\(p = u^{'}(x)\\)，则曲线长度表示为

\\[
J(u) = \int_{a}^{b}\sqrt{1 + p^2}dx 
\\]

证明两点之间直线最短是一个求极小值的问题，要证明一个函数的极小值的“点”（在这里这个“点”还是一个函数），只要证明在函数这个“点”一阶导数为零，二阶导数大于零。下面按照这个套路来进行证明：

#### 一阶导数



> 
> \\[
>  \frac{dJ[u+\xi v] }{d\xi} |_{\xi \to 0} = \frac{dJ[u+\xi v]}{d[u+\xi v]} \cdot \frac{d[u + \xi v]}{d\xi}
>\\]
>
>
> 
> \\[
>  = \frac{dJ[u+\xi v]}{du} \cdot v
>\\]
>
> \\[
> \quad \quad = < \bigtriangledown J;v>     \quad\quad (1)
>\\]

 
 

\\[
h'(\xi)  = \frac{dJ[u+\xi v] }{d\xi} |_{\xi \to 0} = \int_{a}^{b} \frac{d[\sqrt{1 + (u' + \xi v')^2}]}{d\xi}dx  |_{\xi \to 0}
\\]

\\[   
= \int_{a}^{b} v' \frac{u' + \xi v'}{\sqrt{1 + (u' + \xi v')^2}} dx|_{\xi \to 0}
\\]

\\[   
= \int_{a}^{b} v' \frac{u'}{\sqrt{1 + (u')^2}} dx
\\]

\\[   
= v(x)\frac{u'(x)}{\sqrt{1+ (u'(x))^2}}|^{b}_{a} - \int_{a}^{b} v \frac{d[\frac{u'}{\sqrt{1 + (u')^2}}]}{dx} dx \quad\quad (2)
\\]

已知曲线经过(a, \\(\alpha\\))和(b, \\(\beta\\))：
\\[
u(a) = \alpha, \quad u(b) = \beta
\\]

\\[   
\widehat{u}(x) = u(x) + \xi v(x)
\\]

\\(\widehat{u}\\)也必然经过(a, \\(\alpha\\))和(b, \\(\beta\\))，有：

\\[
\widehat{u}(a) = u(a) + \xi v(a) = \alpha
\\]

\\[   
\widehat{u}(b) = u(b) + \xi v(b) = \beta
\\]

所以：

\\[
v(b) = 0, \quad v(a) = 0
\\]

\\[   
 v(x)\frac{u'(x)}{\sqrt{1+ (u'(x))^2}}|^{b}_{a} = 0
 \\]

\\[   
h'(\xi) =   - \int_{a}^{b} v \frac{d[\frac{u'}{\sqrt{1 + (u')^2}}]}{dx} dx \quad\quad 
\\]

\\[   
 = < \bigtriangledown J;v> 
\\]

可以得到一阶导数：

\\[
\bigtriangledown J = - \frac{d}{dx}\frac{u'}{\sqrt{1 + (u')^2}}
\\]

\\[   
= - \frac{u''}{[1 + (u')^2]^{\frac{3}{2}}}
\\]
令一阶导数等于0，得到
\\[
u''(x) = 0
\\]

\\[   
u(x) = cx + d
\\]

此时已经可以看到一阶导数等于0情况下，这条“曲线”就是一条直线，只需再证明二阶导数大于零，问题即可得证


#### 二阶导数


为了便于表示，令：
\\[
m = u' + \xi u'
\\]

\\[   
\frac{dm}{d\xi} = u'
\\]

利用公式（2）的中间结果可知

\\[
h''(\xi) |_{\xi \to 0} = \frac{dh'(\xi)}{d\xi} = \int_{a}^{b} \frac{d}{d\xi}v' \frac{u' + \xi v'}{\sqrt{1 + (u' + \xi v')^2}} dx|_{\xi \to 0}
\\]

\\[   
= \int_{a}^{b} \frac{d}{d\xi} v' \frac{m}{\sqrt{1 + (m)^2}} dx|_{\xi \to 0}
\\]

\\[   
= \int_{a}^{b} v' \frac{v'\sqrt{1+m^2} - \frac{mv'}{\sqrt{1+m^2}}}{1+ m^2}dx|_{\xi \to 0}
\\]

\\[   
=  \int_{a}^{b} (v')^2 \frac{(m-\frac{1}{2})^2 + \frac{3}{4}}{(1+m^2)^{\frac{3}{2}}}dx|_{\xi \to 0}
\\]

\\[   
=  \int_{a}^{b} (v')^2 \frac{(u' -\frac{1}{2})^2 + \frac{3}{4}}{(1+u'^2)^{\frac{3}{2}}}dx
\\]

可以看到\\(h''(x)\\)一定是大于零的，因此直线就是通过两点之间的最短曲线，证毕。

参考资料

<\<Introduction to the calculus of variations>\> Peter J. Olver

https://www.zhihu.com/question/29754921/answer/48219859

https://www.guokr.com/question/512475/


