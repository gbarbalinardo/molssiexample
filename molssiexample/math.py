"""
Math library example
"""
import numpy as np


def euler(n):

    """Function to calculate Euler's number :math:`e` thorugh Taylor series

    .. math::

        e = 1 + \\sum_n^\\infty \\frac{1}{n!}

    Parameters
    ----------
    n : int
        Specify the order of the truncated series

    Returns
    -------
    e_value : float
        Euler number
    """

    if n < 0:
        raise ValueError("Only positive integers are allowed")
    n += 1
    e_value = 0
    for i in range(n):
        e_value += 1 / factorial(i)
    return e_value


def factorial(n):
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1


def pi(mc_points=1e7):

    """Function to calculate :math:`\pi` using Monte-Carlo

    Parameters
    ----------
    mc_points : int
        Specify the number of points for the Monte Carlo integration

    Returns
    -------
    result : float
        Estimated value of :math:`\pi`
    """
    mc_points = int(mc_points)
    x = np.random.uniform(0, 1, mc_points).reshape(-1, 2)
    area = np.sum(np.linalg.norm(x, axis=1) < 1)
    result = (area / mc_points) * 8
    return result