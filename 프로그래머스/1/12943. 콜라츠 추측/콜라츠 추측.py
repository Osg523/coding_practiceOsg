def solution(num):
    answer = 0
    while num != 1:
        if num % 2 == 0:
            answer += 1
            num //= 2
        else:
            answer += 1
            num = num * 3 + 1
        
    if answer > 500:
        answer = -1
    return answer