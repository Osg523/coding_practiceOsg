def solution(s):
    answer = []
    ndic = dict()
    for i, j in enumerate(s):
        if not j in ndic:
            answer.append(-1)
            ndic[j] = i 
        else:
            answer.append(i-ndic[j])
            ndic[j] = i
    return answer