def solution(dartResult):
    answer = 0
    num = []
    dartResult1 = []
    n = 0
    num1 = ''
    for i in dartResult:
        if i.isdigit():
            num1 += i
        if i.isalpha() and num1 != '':
            num.append(int(num1))
            dartResult1.append(num1)
            dartResult1.append(i)
            num1 = ''
        if i == '*' or i == '#':
            dartResult1.append(i)
    for i in dartResult1[1:]:
        if i.isdigit():
            n += 1
        elif i == 'S':
            num[n] = num[n]**1
        elif i == 'D':
            num[n] = num[n]**2
        elif i == 'T':
            num[n] = num[n]**3
        elif i == '*':
            if n == 0:
                num[n] = num[n]*2
            else:
                num[n-1], num[n] = num[n-1]*2, num[n]*2
        else:
            num[n] = num[n]*(-1)
    answer = sum(num)
    return answer