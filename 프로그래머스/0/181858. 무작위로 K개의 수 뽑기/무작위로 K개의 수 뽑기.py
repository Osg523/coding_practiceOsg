def solution(arr, k):
    answer = []
    for i in arr:
        if not i in answer:
            answer += [i]
    if len(answer) < k:
        answer += [-1]*(k-len(set(arr)))
    return answer[:k]