def solution(d, budget):
    answer = 0
    a = 0
    for i in sorted(d):
        a += i
        if a <= budget:
            answer += 1
    return answer