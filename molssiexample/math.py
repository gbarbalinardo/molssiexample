"""
A file for executing math functions.
"""

def euler(last_n):
    e_value = 0
    for i in range(last_n):
        e_value += 1 / factorial(i)
    return e_value


def factorial(n):
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1

