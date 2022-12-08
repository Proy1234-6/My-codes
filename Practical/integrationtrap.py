import numpy as np

def trap(xi,xf,n):
    '''
    x=np.linspace(xi,xf,n)
    h=np.abs(x[0]-x[1])

    y=f(x)
    '''

    yy=[]
    h=(np.abs(xf-xi))/(n-1)

    for i in range(n):
        x=xi+(i*h)
        y= x

        yy.append(y)

    s=0
    for i in range(1,n-1):
        s+= yy[i]
    s=2*s
    s=s+yy[0]+yy[n-1]
    
    return (h/2)*s



xi=0
xf=3
n=20
err=.01
for i in range(2,n+1):
    print("Taking",i,"points the value is-",trap(xi,xf,i))
    
'''
while trap(xi,xf,n+1)-trap(xi,xf,n)>=err:
    print("Taking",n,"points the value is-",trap(xi,xf,n))
    n+=1
'''

    

