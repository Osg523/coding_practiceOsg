from math import gcd
def solution(numer1, denom1, numer2, denom2):
    answer = []
    num = numer1*denom2 + numer2*denom1
    denom = denom1*denom2
    return [num//gcd(num,denom),denom//gcd(num,denom)]