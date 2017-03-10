import numpy as np

def double_gamma(x, lag=6, a2=12, b1=0.9, b2=0.9, c=0.35):
    a1 = lag
    d1 = a1 * b1
    d2 = a2 * b2
    return np.array([(t/(d1))**a1 * np.exp(-(t-d1)/b1) - c*(t/(d2))**a2 * np.exp(-(t-d2)/b2) for t in x])

def single_gamma(x, lag=6, b=0.9):
    a = lag
    d = a * b
    return (x/d)**a * np.exp(-(x-d)/b)