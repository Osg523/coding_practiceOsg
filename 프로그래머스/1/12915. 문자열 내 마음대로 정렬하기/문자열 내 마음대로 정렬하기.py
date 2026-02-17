def solution(strings, n):
    answer = []
    s = set()
    for i in strings:
        s.add(i[n])
    for i in sorted(s):
        a = []
        for j in strings:
            if i == j[n]:
                a += [j]
        answer += sorted(a)
    return answer