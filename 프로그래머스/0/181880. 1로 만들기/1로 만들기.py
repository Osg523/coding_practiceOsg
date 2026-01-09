def solution(num_list):
    answer = 0
    for i in num_list:
        n = i
        while n != 1:
            if n%2:
                n = (n-1)//2
                answer += 1
            else:
                n //= 2
                answer += 1
    return answer