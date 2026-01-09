def solution(s):
    answer = ''
    a = []
    b = []
    a = s.split()
    for i in a:
        b.append(int(i))
    answer += str(min(b)) + " "+ str(max(b))
    return answer