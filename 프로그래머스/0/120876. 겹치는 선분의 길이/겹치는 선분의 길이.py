def solution(lines):
    s = [set(range(l[0], l[1])) for l in lines]
    
    a = s[0] & s[1] 
    b = s[0] & s[2] 
    c = s[1] & s[2] 
    
    total = a | b | c
    
    return len(total)