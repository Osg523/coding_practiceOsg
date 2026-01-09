def solution(myString):
    answer = []
    l = 0
    for i, x in enumerate(myString):
        if x == 'x':
            answer.append(len(myString[l:i]))
            l = i+1
    answer.append(len(myString[l:]))
    return answer