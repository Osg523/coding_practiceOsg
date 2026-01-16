def solution(quiz):
    return ["O" if eval(i[:i.rfind("=")]) == int(i[i.rfind("=")+1:]) else "X" for i in quiz]