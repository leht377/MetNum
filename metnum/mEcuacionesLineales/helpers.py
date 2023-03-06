import numpy as np


def sustregr(T, c):
    T = np.array(T)
    c = np.array(c)

    dim, nc = c.shape
    x = np.zeros((dim, nc))
    for i in range(dim - 1, -1, -1):
        x[i, :] = (c[i, :] - np.dot(T[i, :], x)) / T[i, i]
    return x


def sustprogr(T, c):
    T = np.array(T)
    c = np.array(c)
    dim, nc = c.shape
    x = np.zeros((dim, nc))
    for i in range(dim):
        x[i, :] = (c[i, :] - np.dot(T[i, :], x)) / T[i, i]
    return x
