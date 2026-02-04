def solution(arr, divisor):
    answer = sorted([i for i in arr if not i%divisor]) 
    if not answer:
        return [-1]
    return answer