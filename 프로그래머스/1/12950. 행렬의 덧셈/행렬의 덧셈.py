import numpy as np

def solution(arr1, arr2):
    n1 = np.array(arr1)
    n2 = np.array(arr2)
    n3 = n1+n2
    return n3.tolist()