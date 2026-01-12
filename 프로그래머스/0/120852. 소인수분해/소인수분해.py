def solution(n): 
    answer = []
    i = 2
    while n != 1:
        if n % i == 0:
            n //= i
            if not i in answer:
                answer += [i]
        else:
            i += 1
    return answer