def solution(s):
    answer = 0
    d = {}
    a = 0
    for i, v in enumerate(s):
        d[v] = d.get(v,0) + 1
        if d[s[a]] == sum(d.values())-d[s[a]]:
            a = i+1
            d ={}
            answer += 1
    if d:
        answer += 1
    return answer