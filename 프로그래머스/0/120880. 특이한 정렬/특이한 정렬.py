def solution(numlist, n):
    answer = []
    dic = dict()
    for i in numlist:
        if abs(i-n) in dic:
            dic[abs(i-n)] += [i]
        else:
            dic[abs(i-n)] = [i]
    for i in sorted(dic):
        answer += [j for j in sorted(dic[i], reverse = True)]
    return answer