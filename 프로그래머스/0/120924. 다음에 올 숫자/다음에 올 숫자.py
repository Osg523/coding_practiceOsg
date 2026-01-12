def solution(common):
    x, y, z = common[0], common[1], common[2]
    
    if y - x == z - y:
        d = y - x
        return common[-1] + d
        
    else:
        r = y // x 
        return common[-1] * r