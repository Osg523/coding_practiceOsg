def solution(babbling):
    answer = 0
    a = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        n = 0
        s = ''
        while n <= len(i):
            if (i[n:2+n] in a) and (s != i[n:2+n]):
                s = i[n:2+n]
                n += 2
            elif (i[n:3+n] in a) and (s != i[n:3+n]):
                s = i[n:3+n]
                n += 3
            else:
                break
        if n == len(i):
            answer += 1
    return answer