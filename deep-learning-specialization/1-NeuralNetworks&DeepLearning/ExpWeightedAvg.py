# Exponentially weighted averages
import numpy as np

y = np.array([10, 10])
beta = 0.5


def ewa(y, beta):
    """Exponentially weighted average."""

    n = len(y)
    zs = np.zeros(n)
    z = 0
    for i in range(n):
        z = beta*z + (1 - beta)*y[i]
        zs[i] = z
    return zs


def ewabc(y, beta):
    """Exponentially weighted average with bias correction."""

    n = len(y)
    zs = np.zeros(n)
    z = 0
    for i in range(n):
        z = beta*z + (1 - beta)*y[i]
        zc = z/(1 - beta**(i+1))
        zs[i] = zc
    return zs


exp_w = ewa(y, beta)
corrected_exp_w = ewabc(y, beta)

# for quiz question
print(exp_w[1], corrected_exp_w[1])
