def solution(angle):
    if angle - 90 < 0:
        return 1
    elif angle - 90 == 0:
        return 2
    elif angle - 90 == 90:
        return 4
    else:
        return 3
    return answer