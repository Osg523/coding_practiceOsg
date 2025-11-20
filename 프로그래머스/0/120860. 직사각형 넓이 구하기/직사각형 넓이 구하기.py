def solution(dots):
    answer = 0
    x = 0
    y = 0
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    for i in dots:
        if x1 != i[0]:
            x2 = x1
            x1 = i[0]
            
        if y1 != i[1]:
            y2 = y1
            y1 = i[1]
    if x1 < x2:
        x = x2 - x1
    else:
        x = x1 - x2
    if y1 < y2:
        y = y2 - y1
    else:
        y = y1 - y2
    answer = x*y
    return answer