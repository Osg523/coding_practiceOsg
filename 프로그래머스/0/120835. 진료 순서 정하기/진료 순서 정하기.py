def solution(emergency):
    answer = [0]*len(emergency)
    j = len(emergency)
    for i in sorted(emergency):
        answer[emergency.index(i)] = j
        j -=1
    return answer