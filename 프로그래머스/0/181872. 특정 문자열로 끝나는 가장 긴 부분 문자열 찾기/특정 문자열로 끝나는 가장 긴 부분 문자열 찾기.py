def solution(myString, pat):
    for i in range(len(myString)):
        if myString[:len(myString)-i].endswith(pat):
            return myString[:len(myString)-i]
    return answer