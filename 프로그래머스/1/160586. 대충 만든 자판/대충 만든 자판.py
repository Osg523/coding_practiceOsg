def solution(keymap, targets):
    answer = []
    d = {}
    for i in range(len(keymap)):
        s = keymap[i]
        for j in set(s):
            m =s.find(j)+1
            d[j] = min(d.get(j, m), m) 
    
    for i in targets:
        a = 0
        for j in i:
            if j in d:
                a += d[j]
            else:
                a = 0
                break
        if a:
            answer.append(a)
        else:
            answer.append(-1)
            
    return answer