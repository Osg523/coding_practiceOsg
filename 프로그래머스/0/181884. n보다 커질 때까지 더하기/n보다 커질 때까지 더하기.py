def solution(numbers, n):
    a = 0
    for i in numbers:
        if a <= n:
            a += i
    return a