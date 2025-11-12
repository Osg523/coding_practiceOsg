def solution(s):
    zero = 0
    rou = 0
    while s != '1':
        binScale = ''
        
        one = s.count('1')
        zero += len(s) - one
        rou += 1
        
        while one > 1:
            binScale += str(one%2)
            one = one // 2
        binScale += str(one)
        s = binScale
    answer = [rou, zero]
    return answer





''' 1번째 시도
def solution(s):
    zero = 0
    rou = 0
    while s != '1':
        s1 = ''
        binScale = []
        for i in s:
            if i != '0':
                s1 += i
            else:
                zero += 1
        rou += 1
        a = len(s1)
        while a != 1 or a != 0:
            binScale.append(a%2)
            a = a // 2
        binScale.append(a)
        s = set(binScale.reversed())
    answer = [rou, zero]
    return answer
'''

''' 2번째 시도
def answer(S, ROU, ZERO):
    s1 = ''
    for i in S:
        if i != '0':
            s1 += i
        else:
            ZERO += 1
    ROU += 1
    return s1, ROU, ZERO

def binaryScale(num):
    bin1 = []
    while num != 1 or num != 0:
        bin1.append(num%2)
        num = num // 2
    bin1.append(num)
    s2 = set(bin.reversed())
    return s2

def solution(s):
    zero = 0
    rou = 0
    while s != '1':
        s, rou, zero = answer(s, rou, zero)
        s = binaryScale(len(s))
    answer1 = [rou, zero]
    return answer1
'''
