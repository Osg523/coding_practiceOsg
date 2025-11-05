def solution(s):
    answer = ''
    a = []
    for i in s:
        a.append(i)
        
    a = sorted(a, reverse = True)
    for i in a:
        answer += str(i)
    return answer


""" 이렇게 2개를 따로 써도 되긴함
a.sort()
a.reverse()
"""
