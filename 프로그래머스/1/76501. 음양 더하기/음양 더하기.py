def solution(absolutes, signs):
    answer = 0
    num = []
    for i in range(len(signs)):
        if signs[i] == True:
            num.append(absolutes[i])
        else:
            num.append(-absolutes[i])
    for a in num:
        answer += a
    
    return answer 