import numpy as np
import matplotlib.pyplot as plt

def fibonacci_numbers_up_to(limit):
    fib = [1, 1]
    while fib[-1] < limit:
        fib.append(fib[-1] + fib[-2])
    return fib

def fib_search(f, a, b, eps):
    history = []
    
    L0 = (b - a) / (2 * eps)
    fib = fibonacci_numbers_up_to(L0)
    n = len(fib) - 1

    y = a + fib[n - 2] / fib[n] * (b - a)
    z = a + fib[n - 1] / fib[n] * (b - a)
    f_y = f(y)
    f_z = f(z)

    for k in range(1, n - 1):
        print(np.array([a, y, z, b]))

        if f_y <= f_z:
            b = z
            z = y
            f_z = f_y
            y = a + fib[n - k - 2] / fib[n - k] * (b - a)
            f_y = f(y)
        else:
            a = y
            y = z
            f_y = f_z
            z = a + fib[n - k - 1] / fib[n - k] * (b - a)
            f_z = f(z)

        history.append([a, b])

    return (a + b) / 2, history

def fib_search2(f, a, b, eps):
    history = []
    
    L0 = (b - a) / (2 * eps)
    fib = fibonacci_numbers_up_to(L0)
    n = len(fib) - 1

    z = a + fib[n - 1] / fib[n] * (b - a)
    y = a + b - z
    f_y = f(y)
    f_z = f(z)

    for k in range(1, n - 1):
        print(np.array([a, y, z, b]))

        if f_y <= f_z:
            b = z
            z = y
            f_z = f_y
            y = a + b - z
            f_y = f(y)
        else:
            a = y
            y = z
            f_y = f_z
            z = a + b - y
            f_z = f(z)

        history.append([a, b])
    print(y,z)
    return (a + b) / 2, history

def f(x):
    return x**2 - 2*x + 5

a, b = -2, 8
eps = 0.005

# x_star, history = fib_search(f, a, b, eps)
# print("x* ≈", x_star, "+-", eps)
# print("f(x*) ≈", f(x_star))

# plot_fib(f, a, b, history, x_star)
# print()

x_star, history = fib_search2(f, a, b, eps)
print("x* ≈", x_star, "+-", eps)
print("f(x*) ≈", f(x_star))

