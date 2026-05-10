def solution(N, stages):
    answer = []
    n = len(stages)
    j = {}
    for i in range(1,N+1):
        if n != 0:
            a = stages.count(i)
            j[i] = a/n
            n -= a
        else:
            j[i] = 0
    answer = sorted(j, key = lambda x : j[x], reverse = True)
    return answer