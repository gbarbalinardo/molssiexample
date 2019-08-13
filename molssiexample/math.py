"""
A file for executing math functions.
"""

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

