import numpy as np

def trap(xi,xf,n):
    
    yy=[]
    h=(xf-xi)/(n-1)

    for i in range(n):
        x=xi+(i*h)
        y=np.sin(x)
        yy.append(y)

    s=0
    for i in range(1,n-1):
        s= s+ yy[i]
    s=2*s
    s=s+yy[0]+yy[n-1]
    
    return (h/2)*s

xi=-(np.pi)
xf=np.pi
n=10
for i in range(2,n+1):
    print("Taking ",i,"Points the value is-",trap(xi,xf,i))
