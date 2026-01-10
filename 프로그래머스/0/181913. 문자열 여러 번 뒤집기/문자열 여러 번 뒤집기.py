def solution(my_string, queries):
    m = list(my_string)
    for i, j in queries:
        a = m[i:j+1]
        m = m[:i]+a[::-1]+m[j+1:]
    return ''.join(m)