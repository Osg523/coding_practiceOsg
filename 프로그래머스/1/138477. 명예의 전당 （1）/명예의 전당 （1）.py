def solution(k, score):
    answer,result = [], []
    for i in score:
        if len(answer) < k:
            answer.append(i)
        elif min(answer) <= i:
            answer[answer.index(min(answer))] = i
        result.append(min(answer))
    return result