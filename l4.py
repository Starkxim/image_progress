import sympy
from sympy import I,pi,oo
import numpy as np
import scipy

x=sympy.Symbol('x')
y=sympy.Symbol('y')
z=sympy.Symbol('z')
a,b=sympy.symbols('a,b',positive=True)
'''
#根据x和y的正负，结果不一样
x=sympy.Symbol('x')
y=sympy.Symbol('y',positive=True)
z=sympy.Symbol('z',negative=True)
print(sympy.sqrt(x**2))
print(sympy.sqrt(y**2))
print(sympy.sqrt(z**2))

#根据数的奇偶，结果不一样
n1 = sympy.Symbol('n')
n2 = sympy.Symbol('n', even=True)
n3 = sympy.Symbol('n', odd=True)
print(sympy.cos(n1 * sympy.pi))
print(sympy.cos(n2 * sympy.pi))
print(sympy.cos(n3 * sympy.pi))

#计算分数
a1=sympy.Rational(11,13)
a2=sympy.Rational(5,8)
print(a1+a2)

#计算阶乘
print(np.math.factorial(100))
print(scipy.special.factorial(100))
print(sympy.factorial(100))
print(np.math.factorial(100)==scipy.special.factorial(100))
print(np.math.factorial(100)==sympy.factorial(100))

x,y,z=sympy.symbols('x,y,z')
f=sympy.Function('f')
print(sympy.sin(pi*3/2))
print(sympy.sin(np.pi*3/2))
print(sympy.sin(pi*3/2)==sympy.sin(np.pi*3/2))

#n为整数
n=sympy.Symbol('n',integer=True)
print(sympy.sin(pi*n))

#定义函数
x=sympy.Symbol('x')
h=sympy.Lambda(x,x**2)
print(h(5))
print(h(1+x))

#取函数的一部分
expr=1+2*x**2+3*x**3
print(expr)
print(expr.args)
print(expr.args[1])
print(expr.args[1].args)
print(expr.args[1].args[1])
print(expr.args[1].args[1].args)
print(expr.args[1].args[1].args[0])
print(expr.args[1].args[1].args[0].args)

#化简表达式
a,b=sympy.symbols('a,b',positive=True)
expr1=2*(x**2-x)-x*(x+1)
print(sympy.simplify(expr1))
expr2=2*sympy.cos(x)*sympy.sin(x)
print(sympy.simplify(expr2))
expr3=sympy.exp(x)*sympy.exp(y)
print(sympy.simplify(expr3))

#展开表达式
expr4=(x+1)*(x+2)*(x+3)
print(sympy.expand(expr4))
expr5=sympy.sin(x+y).expand(trig=True)
print(expr5)
expr6=sympy.log(a*b).expand(log=True)
print(expr6)

expr7=sympy.exp(I*a+b).expand(complex=True)
print(expr7)
print(sympy.expand((a+b)**x,power_base=True))
print(sympy.expand((a*b)**x,power_base=True))
print(sympy.exp((a-b)*x).expand(power_base=True))
print(sympy.exp((a-b)*x).expand(power_exp=True))

#
print(sympy.factor(x**3-1))
print(sympy.factor(x**4-1))
print(sympy.logcombine(sympy.log(a)-sympy.log(b)))
expr1=x+y+x*y*z
print(expr1.collect(x))
print(expr1.collect(y))
expr2=sympy.cos(x+y)+sympy.sin(x-y)
print(expr2.expand(trig=True))
print(expr2.expand(trig=True).collect([sympy.cos(x),sympy.sin(x)]))
print(expr2.expand(trig=True).collect([sympy.cos(x),sympy.sin(x)]).collect(sympy.cos(y)-sympy.sin(y)))

print(sympy.apart(1/(x**2+3*x+2),x))
print(sympy.apart(1/(x**3+x**2+3*x+2),x))
print(sympy.apart(1/(x**3+2),x))
print(sympy.apart(1/(x**3-1),x))
print(sympy.together(-(x+2)/(3*(x**2+x+1))+1/(3*(x-1))))
print(sympy.together(1/(y*x+y)+1/(1+x)))
print(sympy.cancel(y/(y*x+y)))
print((x+y).subs(x,y))
print(sympy.sin(x*sympy.exp(x)).subs(x,y))
print(sympy.sin(x*z).subs({z:sympy.exp(y),x:y,sympy.sin:sympy.cos}))
expr=x*y+z**2*x

expr1=x*y+z**2*x
values={x:1.25,y:0.4,z:3.2}
print(expr1.subs(values))
print(sympy.N(pi,50))
print((x+1/pi).evalf(10))
expr2=sympy.sin(pi*x*sympy.exp(x))
print([expr2.subs(x,i).evalf(3) for i in range(10)])

print(sympy.integrate(sympy.sin(x)))
print(sympy.integrate(sympy.exp(-x**2),(x,0,oo)))
print(sympy.integrate(sympy.exp(-x**2),(x,-oo,oo)))
print(sympy.integrate((x+y)**2,x,y))

#泰勒展开
f=sympy.Function('f')(x)
print(sympy.series(f,x))
x0=sympy.Symbol('{x_0}')
print(f.series(x,x0,n=2))
x1=sympy.Symbol('x_1')
print(f.series(x,x1,n=2))
print(f.series(x,x0,n=2).removeO())
print(f.series(x,x0,n=2).removeO().subs(x,x0))
print(sympy.cos(x).series())
print(sympy.exp(x).series())
print((1/(1+x)).series())
print((1/(1+x)).series(n=10))
print((1/(1+x)).series(n=10).removeO())
print(sympy.exp(1/(x+1)).series(n=10).removeO())
print(sympy.exp(1/(x+1)).series(n=10).removeO())
print(sympy.exp(I*x).series(n=10).removeO())

#极限
print(sympy.limit(sympy.sin(x)/x,x,0))
print(sympy.limit(x**x,x,0))
print(sympy.limit(x**x**x,x,0))
f=sympy.Function('f')
h=sympy.Symbol('h')
diff_limit=(f(x+h)-f(x))/h
print(sympy.limit(diff_limit.subs(f,1/x*sympy.sin(x)),h,0))
print(sympy.limit(diff_limit.subs(f,sympy.cos),h,0))
print(sympy.limit(diff_limit.subs(f,sympy.Abs(x)),h,0))
print(sympy.limit(1/x,x,oo))

n=sympy.Symbol('n',integer=True)
x_1=sympy.Sum(1/n**2,(n,1,oo))
print(x_1)
print(x_1.doit())
x_2=sympy.Sum(1/n,(n,1,oo))
print(x_2.doit())
x_3=sympy.Sum(1/sympy.log(n),(n,1,oo))
print(x_3.doit())
x_4=sympy.Product(n,(n,1,100))#注意数字爆炸
print(x_4.doit())

#解关于x的方程
print(sympy.solve(x**2+1,x))
print(sympy.solve(sympy.cos(x),x))
a,b,c=sympy.symbols('a,b,c')
print(sympy.solve(a*x**2+b*x+c,x))
print(sympy.solve(a*x**3+b*x+c,x))
print(sympy.solve(a*x**5-b**2+c,x))
print(sympy.solve(x**5-x**2+1,x))

#解二元方程
eq1=x+y*2-1
eq2=x-y+1
print('s1',sympy.solve([eq1,eq2],[x,y]))
eq1=x**2-y
eq2=y**2-x
sols=sympy.solve([eq1,eq2],[x,y])
print([eq1.subs(sols).simplify()==eq1,eq2.subs(sols).simplify()==eq2])
sols1=sympy.solve([eq1,eq2],[x,y],dict=True)
print(sols1)
print([eq1.subs(sol).simplify()==0 and eq2.subs(sol).simplify()==0 for sol in sols1])
'''

#矩阵
A=sympy.Matrix([[1,2,3],[4,5,6],[7,8,9]])
print(A)
print(A.T)
print(A.det())
print(A.eigenvals())
print(A.eigenvects())
print(A.charpoly())
B=sympy.Matrix(3,4,lambda m,n:10*m+n)
print(B)
a,b,c,d=sympy.symbols('a,b,c,d')
C=sympy.Matrix([[a,b],[c,d]])
print(C)
print(C*C)
D=sympy.Matrix(sympy.symbols('x_1,x_2'))
print(D)
print(C*D)
E=sympy.Matrix(sympy.symbols('e_1,e_2'))
e=C.LUsolve(E)
f=C.inv()*E
print(e)
print(f)
print(C.QRdecomposition())
print(E.QRsolve(b))
