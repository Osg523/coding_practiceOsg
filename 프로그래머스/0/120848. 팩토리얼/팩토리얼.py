def solution(n):
    answer = 0
    i = 1
    while i <= n:
        answer += 1
        i *= answer
    return answer-1