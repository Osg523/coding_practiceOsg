def solution(dot):
    answer = 0
    if dot[0] > 0:
        if dot[1] > 0:
            answer = 1
        else:
            answer = 4
    else:
        if dot[1] < 0:
            answer = 3
        else:
            answer = 2
    return answer

#solution = lambda dot: 1 if dot[0] > 0 and dot[1] > 0 else 4 if dot[0] > 0 else 2 if dot[1] > 0 else 3
