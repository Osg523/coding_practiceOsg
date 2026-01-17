def solution(a, b, c, d):
    answer = 0
    dic = dict()
    for i in [a,b,c,d]:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    dk = list(dic.keys())
    dv = list(dic.values())
    if len(dic) == 1:
        answer = 1111*a
    elif len(dic) == 2 and 3 in dv:
        if dv[0] == 3:
            answer = (10*dk[0]+dk[1])**2
        else:
            answer = (10*dk[1]+dk[0])**2
    elif len(dic) == 2:
        answer = (sum(dk))*abs(dk[0]-dk[1])
    elif len(dic) == 3:
        if dv[0] == 2:
            answer = dk[1]*dk[2]
        elif dv[1] == 2:
            answer = dk[0]*dk[2]
        else:
            answer = dk[0]*dk[1]
    else:
        answer = min(dk)
            
    
    return answer