import numpy as np
def solution(a, b):
    n1 = np.array(a)
    n2 = np.array(b)
    return int(np.dot(n1,n2))