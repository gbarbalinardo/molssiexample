"""
A file for executing math functions.
"""

import numpy as np

def euler(last_n):
    if last_n < 0:
        raise ValueError("Only positive integers are allowed")
    last_n += 1
    e_value = 0
    for i in range(last_n):
        e_value += 1 / factorial(i)
    return e_value


def factorial(n):
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1


def pi(mc_points):
    x = np.random.uniform(0, 1, mc_points)
    y = np.random.uniform(0, 1, mc_points)
    area = 0
    for i in range(mc_points):
        x_value = x[i]
        y_value = y[i]
        if (x_value ** 2 + y_value ** 2) <= 1:
            area += 1
    return (area / mc_points)


