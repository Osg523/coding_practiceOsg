def solution(s):
    answer = ''
    i = 0
    for j in s:
        if j == ' ':
            answer += ' '
            i = 0
        else:
            if i%2:
                answer += j.lower()
            else:
                answer += j.upper()
            i += 1
    return answer