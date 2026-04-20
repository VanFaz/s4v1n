import numpy as np
import matplotlib.pyplot as plt

def dichotomy(f, a, b, eps, delta):
    history = []
    
    while (b - a) > 2*eps:    
        y = (a+b-delta)/2
        z = (a+b+delta)/2
        print(np.array([a,y,z,b]))
        if f(y) <= f(z):
            b = z
        else:
            a = y
        
        history.append([a,b])
    
    return (a+b)/2, history

def f(x):
    return x**2 - 2*x + 5

a, b = -2, 8
eps = 0.5
delta = 0.2

x_star, history = dichotomy(f, a, b, eps, delta)
print("x* ≈", x_star,'+-',eps)
print("f(x)* ≈", f(x_star))

        