def solution(ineq, eq, n, m):
    answer = 0
    if eq == '=':
        return int(eval(str(n)+ineq+eq+str(m)))
    else:
        return int(eval(str(n)+ineq+str(m)))
    return answer