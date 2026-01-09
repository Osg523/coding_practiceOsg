def solution(triangle):
    alist = {}
    b = 0
    for i in triangle:
        b += 1
        list1 = []
        if b == 1:
            list1 = i
        else:
            prev = alist[b - 1]
            for a in range(len(i)):
                if a - 1 >= 0:
                    l = prev[a - 1]  
                else:
                    l = 0
                if a < len(prev):
                    r = prev[a]
                else:
                    r = 0
                list1.append(i[a] + max(l, r))
        alist[b] = list1

    return max(alist[b])
