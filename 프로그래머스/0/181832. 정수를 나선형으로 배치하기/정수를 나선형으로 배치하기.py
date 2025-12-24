def solution(n):
    answer = []
    for i in range(n):
        one = []
        for j in range(n):
            one.append(0)
        answer.append(one)

    i = 0
    j = 0

    top = 0
    bottom = n - 1
    left = 0
    right = n - 1

    k = 1
    while k <= n * n:
        for j in range(left, right + 1):
            answer[top][j] = k
            k += 1
        top += 1

        for i in range(top, bottom + 1):
            answer[i][right] = k
            k += 1
        right -= 1

        if top <= bottom:
            for j in range(right, left - 1, -1):
                answer[bottom][j] = k
                k += 1
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                answer[i][left] = k
                k += 1
            left += 1

    return answer
