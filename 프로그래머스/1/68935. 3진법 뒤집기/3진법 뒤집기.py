def solution(n):
    answer = 0
    t = ''
    while n >= 1:
        t += str(n % 3)
        n //= 3
    return int(t,3)
