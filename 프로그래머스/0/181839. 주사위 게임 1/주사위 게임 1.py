def solution(a, b):
    if (a*b)%2:
        return a**2+b**2  
    elif (a+b)%2:
        return 2*(a+b)
    else:
        return abs(a-b)
    return answer
