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