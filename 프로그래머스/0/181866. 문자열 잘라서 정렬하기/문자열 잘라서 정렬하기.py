def solution(myString):
    a = ''.join(i for i in myString.split(' '))
    answer = sorted(a.split('x'))
    while '' in answer:
        answer.remove('')
            
    return answer