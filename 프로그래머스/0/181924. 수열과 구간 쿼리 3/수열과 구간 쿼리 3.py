def solution(arr, queries):
    answer = []
    for a,b in queries:
        arr[a], arr[b] = arr[b], arr[a]
            
    answer =arr
    return answer