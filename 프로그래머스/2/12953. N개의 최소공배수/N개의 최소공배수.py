def solution(arr):
    answer = 1
    nl1 = set()
    
    for i in range(2, 101): 
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):  
            if i % j == 0:  
                is_prime = False
                break
        if is_prime:
            nl1.add(i)
    
    sl = []

    for i in arr:
        d = {}
        n = i
        for p in nl1:
            cnt = 0
            while n % p == 0:
                n //= p
                cnt += 1
            if cnt > 0:
                d[p] = cnt
        sl.append(d)


    max_exp = {}
    for d in sl:
        for k in d:
            if k not in max_exp or d[k] > max_exp[k]:
                max_exp[k] = d[k]


    for k in max_exp:
        answer *= k ** max_exp[k]

    return answer



'''
def solution(arr):
    answer = 1
    sl = []
    nl = []
    nl1 = []
    nl1 = set()

    for i in range(2, 101): 
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):  
            if i % j == 0:  
                is_prime = False
                break
        if is_prime:
            nl1.add(i)
            
    for i in arr:
        s = set()
        for n in nl1:
            if i % n == 0:
                s.add(n)
        sl.append(s)
    s = sl[0]
    for i in sl[1:]:
        s = s&i
    for i in arr:
        n = i
        for j in s:
            n = n // j
        nl.append(n)
    for i in nl:
        answer *= i
    for i in s:
        answer *= i
        
    return answer
'''
