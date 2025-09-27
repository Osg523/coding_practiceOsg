def solution(arr, queries):
    answer = []
    for query in queries:
        i = query[0]
        j = query[1]
        a = arr[i]
        arr[i] = arr[j]
        arr[j] = a
            
    for i in arr:
        answer.append(i)
    return answer