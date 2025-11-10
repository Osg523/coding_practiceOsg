def solution(s, n):
    answer = ''
    alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    for i in s:
        if i in alp:
            n1 = alp.index(i)
        else:
            n1 = -1

        if n1 == -1:
            answer += i
        elif i.islower():
            base = alp.index('a') 
            idx = (n1 + n) % 26 + base
            answer += alp[idx]
        else:  
            base = alp.index('A')  
            idx = (n1 + n) % 26 + base
            answer += alp[idx]

    return answer
