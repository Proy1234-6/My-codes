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
    return 1- abs(x)
#transform for even function
def g(n):
    return np.sqrt(2/np.pi) * simp(-1,1,1001,lambda x: f(x)*np.cos(n*x))
#ploting
n=np.linspace(-15,15,1000)
p=np.linspace(-1,1,100)
y=g(n)
y1=f(p)
plt.plot(n,y,'r',label = "F-T")
plt.plot(p,y1,'g',label = "F(x)")
plt.xlabel("X", size = 20)
plt.ylabel("F(x)",size = 20)
plt.legend(loc = 'best')
plt.axhline()
plt.show()
