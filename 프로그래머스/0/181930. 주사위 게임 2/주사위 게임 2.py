def solution(a, b, c):
    return a+b+c if (a != b and b != c and c != a) else (a*3)*(a**2*3)*(a**3*3) if a*3 == a+b+c else (a+b+c)*(a**2+b**2+c**2)