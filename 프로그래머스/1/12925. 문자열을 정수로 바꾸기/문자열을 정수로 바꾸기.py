def solution(s):
    if s[0] == "-":
        answer = -int(s[1:])
    else:
        answer = int(s)
    return answer

# answer = int(s) 만 해도 됨
