import numpy as np
import matplotlib.pyplot as plt
def trap(xi,xf,n):

    yy=[]
    xx=[]
    h =(xf-xi)/(n-1)

    for i in range(n):
        x=xi + (i*h)
       
        y= np.exp(x)
        yy.append(y)

    s= 0
    for i in range(1,n-1):
        s+= yy[i]
    s=2*s
    s=yy[0]+s+yy[n-1]

    s=.5*s*h

    return s

xi=-2.76
xf=2.76
n=2

err=.01
y1=[]
y2=[]
while trap(xi,xf,n) - trap(xi,xf,n+1)>=err:
    print("Taking ",n,"points, the value is-",trap(xi,xf,n))
    g=trap(xi,xf,n)
    y2.append(g)
    y1.append(n)
    n=n+1


#xi=-2.76
#xf=2.76
#n=

#for i in range(2,n+1):
    #print('for -',i,'points value -',trap(xi,xf,i)[0])


#x=trap(xi,xf,n)[1]
#y=trap(xi,xf,n)[2]

#plt.plot(x,y)
#plt.subplot(121)
#plt.title('The function')
#plt.xlabel('Values of x')
#plt.ylabel('e^x value')

#plt.subplot(122)
plt.plot(y1,y2)
plt.title('The error graph')
plt.xlabel('The number of points')
plt.ylabel('The value')


plt.show()



