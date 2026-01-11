def solution(score):
    s = [sum(i) for i in score]
    rank = {}
    k = len(score)
    for i in sorted(set([sum(i) for i in score])):
        c = s.count(i)
        k -= c
        rank[i] = k+1
    return [rank[i] for i in s]