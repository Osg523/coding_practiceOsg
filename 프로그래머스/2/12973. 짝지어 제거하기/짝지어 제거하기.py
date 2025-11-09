def solution(s):
    if len(s) & 1:
        return 0

    a = list(s)  
    top = -1        
    i = 0            

    while i < len(a):
        if top >= 0 and a[top] == a[i]:
            top -= 1           
        else:
            top += 1            
            a[top] = a[i]       
        i += 1

    return 1 if top == -1 else 0
