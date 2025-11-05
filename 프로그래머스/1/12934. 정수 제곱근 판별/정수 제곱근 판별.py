import math
def solution(n):
    answer = 0
    x = math.sqrt(n)
    if x == int(x):
        answer = math.pow(x+1, 2)
    else:
        answer = -1
    return answer


""" math 함수 사용 안하고 싶을 때 코드
def solution(n):
    answer = 0
    x = n**0.5
    if x == int(x):
        answer = (x+1)**2
    else:
        answer = -1
    return answer
"""
