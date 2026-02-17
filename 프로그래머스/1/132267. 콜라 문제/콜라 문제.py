def solution(a, b, n):
    answer = 0
    an = 0
    while n >= a:
        if not n%a:
            answer += b*(n//a)
            n = n//a*b
        else:
            an = n%a
            answer += b*(n//a)
            n = n//a*b + an
    return answer