def solution(participant, completion):
    par = {}
    com = {}
    
    for i in participant:
        par[i] = par.get(i, 0) + 1
    
    for i in completion:
        com[i] = com.get(i, 0) + 1
    
    for i in par:
        if par[i] != com.get(i, 0):
            return i
