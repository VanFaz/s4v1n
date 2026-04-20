import numpy as np
import matplotlib.pyplot as plt

def gold(f, a, b, eps):
    history = []
    phi = (np.sqrt(5) - 1) / 2  
    
    y = b - phi * (b - a)
    z = a + phi * (b - a)
    f_y = f(y)
    f_z = f(z)

    while (b - a) > 2 * eps:
        print(np.array([a, y, z, b]))

        if f_y <= f_z:
            b = z
            z = y
            f_z = f_y
            y = b - phi * (b - a)
            f_y = f(y)
        else:
            a = y
            y = z
            f_y = f_z
            z = a + phi * (b - a)
            f_z = f(z)

        history.append([a, b])

    return (a + b) / 2, history

def plot_gold(f, a, b, history,x_star):
    x = np.linspace(a, b, 400)
    plt.plot(x, f(x))
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='black', linewidth=0.5, alpha=0.7)
    plt.axvline(x=0, color='black', linewidth=0.5, alpha=0.7)
    plt.scatter(x_star,f(x_star), color='r')
    for a,b in history:
        plt.axvline(a, linestyle="--", alpha=0.5)
        plt.axvline(b, linestyle="--", alpha=0.5)
    plt.show()


def f(x):
    return x**2 * np.log(x)

a, b = 0.1, 100
eps = 0.005

x_star, history = gold(f, a, b, eps)
print("x* ≈", x_star,'+-',eps)
print("f(x)* ≈", f(x_star))

plot_gold(f, a, b, history,x_star)
    