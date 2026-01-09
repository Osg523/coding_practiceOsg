def solution(array, height):
    i = 0
    for a in array:
        if a > height:
            i += 1
    return i