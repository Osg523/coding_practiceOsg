def solution(numbers, k):
    answer = 0
    a = 0
    for i in range(k-1): #0,1,2
        a += 2
        answer = numbers[(a)%len(numbers)]
    return answer