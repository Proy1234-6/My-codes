import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = x**3 -3*(x**2)+2*x
    return y


def df(x):
    y = 3*(x**2) - 6*x +2
    return y
 
x = 0.9
t= .0001
h= f(x)/df(x)

while abs(f(x)) > t:
    
    h= f(x)/df(x)
    x=x-h

print(x)

xx=np.linspace(-.5,2.5,500)
yy=f(xx)


plt.plot(xx,yy,'--',label='Graph of Function')
plt.title("The Graph of the function and it's root")
plt.text(x,0.01,f"The root is at ({x :.1f})")
plt.plot(x,0, 'ro')
plt.legend(loc="best")
plt.xlabel('Value of x')
plt.ylabel('Value of f(x)')
plt.axhline()
plt.grid()
plt.show()
