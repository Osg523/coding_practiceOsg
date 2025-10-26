def solution(n):
    answer = 0
    for i in range(n+1):
        if i == 0:
            n1 = 0
        elif i == 1:
            n2 = 1
        else:
            n3 = n1 + n2
            n1 = n2
            n2 = n3
    
    answer = n3 % 1234567
        
    return answer