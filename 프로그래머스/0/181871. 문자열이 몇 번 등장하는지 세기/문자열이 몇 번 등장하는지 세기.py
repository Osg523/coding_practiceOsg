def solution(myString, pat):
    answer =0
    a = ""
    for i in range(len(myString)):
        a = myString[i:len(pat)+i]
        if pat in a:
            answer += 1
        
        
    return answer