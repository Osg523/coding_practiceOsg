def solution(sides):
    answer = len(range(max(sides)-min(sides),max(sides)))+len(range(max(sides)+1,sides[0]+sides[1]))
    
    return answer