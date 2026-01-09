def solution(arr, flag):
    answer = []
    for i,j in enumerate(flag):
        if j:
            answer += [arr[i]]*arr[i]*2
        else:
            answer = answer[:len(answer)-arr[i]]
    return answer