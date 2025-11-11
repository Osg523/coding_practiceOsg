def solution(babbling):
    answer = 0
    can = ["aya","ye","woo","ma"]
    for i in babbling:
        s = ''
        n = []
        for j in can:
            n.append(i.find(j))
        n.sort()
        for h in n:
            if h != -1:
                if i[h] == 'a' or i[h] == 'w':
                    s += i[h:h+3]
                else:
                    s += i[h:h+2]
        if i == s:
            answer += 1
    return answer