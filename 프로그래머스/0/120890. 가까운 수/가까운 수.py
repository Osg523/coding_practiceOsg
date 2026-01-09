def solution(array, n):
    minindex = 0
    minvalue = 10000000
    for j, i in enumerate(sorted(array)):
        if minvalue > abs(i-n):
            minindex = j
            minvalue = abs(i - n)
    return sorted(array)[minindex]