def solution(arr, queries):
    for i in queries:
        for i2 in range(i[0],i[1]+1):
            arr[i2] += 1
    return arr