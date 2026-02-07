def coUnt(a):
    c = 0
    for i in range(1,int(a**0.5)+1):
        if not a%i:
            c += 1
            if i*i != a:
                c += 1
    return c

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        c1 = coUnt(i)
        if not c1 % 2:
            answer += i
        else:
            answer -= i
    return answer