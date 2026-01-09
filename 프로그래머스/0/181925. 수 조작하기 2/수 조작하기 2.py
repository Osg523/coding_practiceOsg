def solution(numLog):
    dic = {'w':1,'s':-1,'d':10,'a':-10}
    a = numLog[0]
    answer = ''
    for i in numLog[1:]:
        if a+dic['w'] == i:
            answer += 'w'
        elif a+dic['s'] == i:
            answer += 's'
        elif a+dic['d'] == i:
            answer += 'd'
        else:
            answer += 'a'
        a = i
    return answer