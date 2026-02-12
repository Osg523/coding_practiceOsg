def solution(arr):
    answer = []
    n = -1
    for i in arr:
        if n != i:
            answer += [i]
        n = i
    return answer