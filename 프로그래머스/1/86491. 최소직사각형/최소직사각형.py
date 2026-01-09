def solution(sizes):
    a = []
    ans = []
    b = 1
    c = 1
    for i in sizes:
        if i[0] > i[1]:
            a.append(i[0])
            a.append(i[1])
        else:
            a.append(i[1])
            a.append(i[0])
        ans.append(a)
        a = []
    for i in ans:
        if i[0] >b:
            b = i[0]
        if i[1] > c:
            c = i[1]
    return b*c