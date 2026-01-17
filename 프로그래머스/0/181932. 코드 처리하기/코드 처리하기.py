def solution(code):
    answer = ''
    mode = 0
    for i,j in enumerate(code):
        if j == '1':
            if mode:
                mode = 0
            else:
                mode = 1
        else:
            if mode and i%2:
                answer += j
            elif not mode and not i%2:
                answer += j
    
    return answer if answer else "EMPTY"