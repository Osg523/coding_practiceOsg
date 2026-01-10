def solution(chicken):
    answer = 0
    while chicken >= 10:
        ㅁ = chicken // 10  
        ㅠ = chicken % 10   
        
        answer += ㅁ        
        
        chicken = ㅁ + ㅠ  
        
    return answer
    return answer
