def fato(a):
    o = 1
    for i in range(1,a+1):
        o *= i
    return o

def solution(balls, share):
    answer = fato(balls) // (fato(share)*fato(balls-share))
    return answer