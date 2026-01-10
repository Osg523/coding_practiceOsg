def solution(arr):
    answer = []
    for i in arr:
        if len(answer) and answer[-1] == i:
            answer.pop()
        else:
            answer.append(i)
    return answer if len(answer) else [-1]