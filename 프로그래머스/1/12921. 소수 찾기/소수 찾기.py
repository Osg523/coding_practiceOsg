def solution(n):
    answer = 0
    for i in range(2,n+1):
        p = 0
        if i%2 and i%3 and i%5 and i%7 and i%11 and i%13:
            for j in range(1,int(i**0.5)+1):
                if not i%j:
                    p += 1
                    if j**2 != i:
                        p += 1
        if not p-2 or i==2 or i==3 or i==5 or i==7 or i==11 or i==13:
            answer += 1
    return answer