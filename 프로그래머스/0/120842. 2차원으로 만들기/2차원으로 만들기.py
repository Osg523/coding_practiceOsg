import numpy as np
def solution(num_list, n):
    answer = np.array(num_list,int).reshape(-1,n)
    return answer.tolist()