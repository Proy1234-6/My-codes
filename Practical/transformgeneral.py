import numpy as np

import matplotlib.pyplot  as plt

#simpson method for integration
def simp(xi,xf,n,f):
    yy=[]
    h=(xf-xi)/(n-1)

    for i in range(n):
        x=xi+(i*h)
        y=f(x)
        yy.append(y)

    s1 = 0
    for i in range(1,n-1,2):
        s1+=yy[i]
    s1=s1*4

    s2 = 0
    for i in range(2,n-2,2):
        s2+=yy[i]
    s2=s2*2

    s=yy[0]+s1+s2+yy[n-1]
    s=(h/3)*s
    return s
#function
def f(x):
    if 0<x<1 : return x
    if 1<x<2 : return (2-x)
    if x>2 : return 0
    else: return 0
#transform for even function
def u(n):
    return np.sqrt(2/np.pi) * simp(-1,1,1001,lambda x: f(x)*np.cos(n*x))
def v(n):
    return np.sqrt(2/np.pi) * simp(-1,1,1001,lambda x: f(x)*np.sin(n*x))
def g(n):
    return np.sqrt(u(n)**2 + v(n)**2)
xf =15
xi =-15
x=[]
y=[]
y1=[]
y2=[]
y3=[]
n=10
p = 1000
h= (xf - xi)/(p-1)
while xi <=xf :
    x.append(xi)
    a=u(xi)
    y.append(a)
    b=f(xi)
    y1.append(b)
    c=v(xi)
    y2.append(c)
    d=g(xi)
    y3.append(d)
    xi+=h




#ploting
#n=np.linspace(-15,15,1000)
#p=np.linspace(-1,1,100)
#y=g(n)
#y1=f(p)
plt.plot(x,y,'--r',label = "F-cosine-T")
plt.plot(x,y1,'g',label = "F(x)")
#plt.ylim(-.1,1.2)
plt.plot(x,y2,'--y',label = "F-Sine-T")
plt.plot(x,y3,'--c',label = "F-T")
plt.grid()
plt.xlabel("X", size = 20)
plt.ylabel("F(x)",size = 20)
plt.legend(loc = 'best')
plt.axhline()
plt.show()
