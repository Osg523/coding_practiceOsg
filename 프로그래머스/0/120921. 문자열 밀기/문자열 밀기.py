def solution(A, B):
    answer = 0
    NewA = A
    while B != NewA:
        answer += 1
        NewA = A[-answer:]+A[:-answer]
        if answer == len(A):
            return -1
    return answer