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

# 다른 사람이 푼 코드 배울 점 
# def solution(arr, queries):
#     answer = []
#     for a,b in queries:
#         arr[a], arr[b] = arr[b], arr[a]
            
#     answer =arr
#     return answer
