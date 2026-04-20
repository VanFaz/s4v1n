import numpy as np
import matplotlib.pyplot as plt

def swann(f, x0, t=1e-2):
    history=[x0]
    f_l = f(x0 - t)
    f_m = f(x0)
    f_r = f(x0 + t)

    if f_l >= f_m <= f_r:
        return [x0 - t, x0 + t], history

    if f_l <= f_m >= f_r:
        print('Не удалось построить интервал')
        return

    if f_l >= f_m >= f_r:
        delta = t
        a0 = x0
        xk = x0 + t
    else:
        delta = -t
        b0 = x0
        xk = x0 - t
    history.append(xk)
    k = 1

    while True:
        x_next = xk + 2**k * delta
        history.append(x_next)
        if f(x_next) < f(xk):
            if delta > 0:
                a0 = xk
            else:
                b0 = xk

            xk = x_next
            k += 1
        else:
            if delta > 0:
                b0 = x_next
            else:
                a0 = x_next
            break


    return [a0, b0], history

def f(x):
    return np.cos(x)

result, history = swann(f, 2)
print(f'Интервал: {result}')
print(f'Точки: {history}')
print(f'Итераций: {len(history) - 1}')
