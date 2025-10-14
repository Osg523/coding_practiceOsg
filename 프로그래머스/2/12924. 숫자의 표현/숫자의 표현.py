def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        a = 0
        for j in range(i,n+1):
            a += j
            if n == a:
                answer += 1
                break
            elif n < a:
                break
    return answer