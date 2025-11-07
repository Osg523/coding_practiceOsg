def solution(sizes):
    small,big = [],[]
    for i, j in sizes:
        c = i
        if i > j: i,j = j,c
        small.append(i); big.append(j)
    return max(small) * max(big)