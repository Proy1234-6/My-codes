import numpy as np
import time as t

#st = t.time()

def f(x):
    return x**3 - 27
xi = 2
xf = 4
xdiff = 1
if f(xi)*f(xf)<0:   
    while xdiff  > 0.0001:
        Xa = (xi + xf)/2
        fi = f(xi)
        fa = f(Xa)
        if f(xf) * f(Xa) == 0:
            print("Root is-",Xa )
            break
        elif f(xi) * f(Xa) < 0:
            xf = Xa
        else:
            xi,fi = Xa,fa
        nXa = (xi + xf)/2
        xdiff = abs(f(nXa) - f(Xa))
    print("The root is -",Xa)
else:
    print("Take new limits - ")
    
#et = t.time()

#time = et - st
