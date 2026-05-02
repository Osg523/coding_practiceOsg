def solution(k, m, score):
    answer = 0
    re_score = sorted(score)
    for i in range(len(re_score)//m):
        boxlist = []
        for j in range(m):
            boxlist.append(re_score.pop())
        answer += min(boxlist)*m
    return answer