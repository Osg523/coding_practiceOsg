def solution(sizes):
    small,big = [],[]
    for i, j in sizes:
        c = i
        if i > j: i,j = j,c
        small.append(i); big.append(j)
    return max(small) * max(big)


'''
다른 친구가 푼 코드인데 런타임 에러가 떠서 확인해봄
def solution(sizes):
    a = []
    ans = []
    b = 0
    c = 0
    for i in sizes:
        if i[0] > i[1]:
            a.append(i[0])
            a.append(i[1])
        if i[0] < i[1]:      #이 줄 떄문이였음 if을 else로만 바꾸면 됨
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
'''
