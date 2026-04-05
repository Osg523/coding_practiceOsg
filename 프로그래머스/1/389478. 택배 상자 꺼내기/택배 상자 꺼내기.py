def solution(n, w, num):
    a = [0]*w
    b = []
    c = 0
    v = 1
    for i in range(n):
        if not i%w: v ^= 1
        if v: a[-(i%w+1)] += 1
        else: a[i%w] += 1
        if i+1 == num:
            for j in a: b.append(j) 
            if v: c = -(i%w+1)
            else: c = i%w
    return a[c]-b[c]+1