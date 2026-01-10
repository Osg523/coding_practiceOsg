def solution(arr):
    answer = -1
    arr2 = []
    while arr != arr2:
        arr2 = [i for i in arr]
        answer += 1
        for i, j in enumerate(arr):
            if j >= 50 and not j%2:
                arr[i] = j//2
            elif j < 50 and j%2:
                arr[i] = j*2 + 1
    return answer