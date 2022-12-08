import numpy as np

def simp(xi,xf,n):
    yy=[]
    h=(xf-xi)/(n-1)

    for i in range(n):
        x=xi+(i*h)
        y=x**2
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

xi=0
xf=1
n=10

for i in range(3,n+1):
    print("Taking ",i,"Points the value is-",simp(xi,xf,i))
