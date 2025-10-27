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