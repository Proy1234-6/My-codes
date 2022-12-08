import matplotlib.pyplot as plt
import numpy as np

xx=[0]
yy=[1]

a=0
b=5
n=20

y0 = 1
x0 = 0
h=(b-a)/n
while h<=5:
    
    x=h
    xx.append(x)
    y1 = y0 + ((b-a)/n) *(-y0)
    yy.append(y1)
    y0=y1
    h+=(b-a)/n

x1=[]
y1=[]
h=0
for i in xx:
    y=np.exp(-i)
    y1.append(y)
plt.figure(figsize=(16, 20))
plt.plot(xx,y1, 'g',label = "Original")
plt.plot(xx,yy,'--r', label = "Calculated")
plt.legend(loc="best")
plt.title('The graph of E^-x Vs dy/dx = -y')
plt.xlabel("Value of x",size = 20)
plt.ylabel("Function", size = 20)
plt.show()
