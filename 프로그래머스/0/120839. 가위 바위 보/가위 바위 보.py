def solution(rsp):
    a=""
    for i in rsp:
        if i == "2": i = "0"
        elif i == "0": i = "5"
        else: i = "2"
        a += i
    return a