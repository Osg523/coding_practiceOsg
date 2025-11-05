def solution(s):
    answer = ''
    a = []
    for i in s:
        a.append(i)
        
    a = sorted(a, reverse = True)
    for i in a:
        answer += str(i)
    return answer