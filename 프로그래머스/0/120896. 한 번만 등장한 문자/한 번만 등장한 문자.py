def solution(s):
    dic = dict()
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return ''.join(sorted([j for j, i in dic.items() if i==1]))