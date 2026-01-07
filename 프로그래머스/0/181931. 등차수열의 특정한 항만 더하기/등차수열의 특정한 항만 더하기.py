def solution(a, d, included):
    b = 0
    for i, j in enumerate(included):
        if j:
            b += a + i*d
    return b