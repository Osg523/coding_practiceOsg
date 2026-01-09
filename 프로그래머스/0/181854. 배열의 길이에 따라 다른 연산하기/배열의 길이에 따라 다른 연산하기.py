def solution(arr, n):
    answer = [arr[i]+n if (i+1)%2 else arr[i] for i in range(len(arr))] if len(arr)%2 else  [arr[i]+n if i%2 else arr[i] for i in range(len(arr))]
    return answer