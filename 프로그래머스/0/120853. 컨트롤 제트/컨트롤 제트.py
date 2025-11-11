def solution(s):
    answer = 0
    zl = []
    sl = s.split()
    for i in range(len(sl)):
        if sl[i] == 'Z':
            zl.append(i)
    
    for i in range(len(sl)):
        if i in zl:
            answer -= int(sl[i-1])
        else:
            answer += int(sl[i])
    return answer
