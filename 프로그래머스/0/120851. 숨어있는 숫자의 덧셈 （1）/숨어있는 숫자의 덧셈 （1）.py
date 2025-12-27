def solution(my_string):
    answer = 0
    for i in my_string:
        if i < 'A':
            answer += int(i)
    return answer