import numpy as np

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


def a(n):
    if n==0:
        s = simp(-np.pi,0,1001,lambda x: abs(x))/np.pi + simp(0,np.pi,1001,lambda x: x)/np.pi
        return s
    else:
        s = simp(-np.pi,0,1001,lambda x: abs(x)*np.cos(n*x))/np.pi + simp(0,np.pi,1001,lambda x: x*np.cos(n*x))/np.pi
        return s

def b(n):
    s = simp(-np.pi,0,1001,lambda x: abs(x)*np.sin(n*x))/np.pi + simp(0,np.pi,1001,lambda x: x*np.sin(n*x))/np.pi
    return s


#fourier series
def fourierseries(x,n):
    fourier = a(0)/2
    for i in range(1,n-1):
        fourier = fourier + a(i)*np.cos(i*x) + b(i)*np.sin(i*x)
    return fourier

x= np.linspace(-3*np.pi,3*np.pi,1000)
y1=fourierseries(x,5)
y2=fourierseries(x,3)
y3=fourierseries(x,10)
y4=fourierseries(x,4)

import matplotlib.pyplot as plt

plt.figure(figsize=(16, 15))
plt.subplot(211)
plt.plot(x,y1,"--", label = "5 terms")
plt.plot(x,y2, label = "3 terms")
plt.legend(loc='best')
plt.xlabel(r"$x$", size = 20)
plt.ylabel(r"$f(x)$", size = 20)
plt.title("Triangular wave")
plt.subplot(212)
plt.plot(x,y3,'-g',label = "10 terms")
plt.plot(x,y4,'--r',label = "4 terms")
plt.legend(loc = 'best')
plt.xlabel(r"$x$", size = 20)
plt.ylabel(r"$f(x)$", size = 20)
plt.title("Triangular wave")
plt.show()
