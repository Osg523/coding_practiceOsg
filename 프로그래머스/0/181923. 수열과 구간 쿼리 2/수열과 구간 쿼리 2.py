def solution(arr, queries):
    answer = [ -1 if not [arr[j] for j in range(i[0],i[1]+1) if arr[j] > i[2]] else min([arr[j] for j in range(i[0],i[1]+1) if arr[j] > i[2]]) for i in queries]
                
    return answer