def count1(a):
    l1 = 0
    for i in range(1,int(a**0.5)+1):
        if not a%i:
            l1 += 1
            if i**2 != a:
                l1 += 1
    return l1

def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        c = count1(i)
        if c <= limit:
            answer += c
        else:
            answer += power 
    return answer