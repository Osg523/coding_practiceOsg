def solution(food):
    answer = ''
    for i,j in enumerate(food[1:]):
        answer += str(i+1)*(j//2)
    i = answer 
    answer += '0' + i[::-1]
    
    return answer