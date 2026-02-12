import math
def solution(n, m):
    g = math.gcd(n,m)
    answer = [g, g*(n//g)*(m//g)]
    
    return answer