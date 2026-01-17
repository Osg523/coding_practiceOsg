def solution(array):
    dic = dict()
    for i in array:
        if i not in dic:
            dic[i] = array.count(i)
    dk = list(dic.keys())
    dv = list(dic.values())
    if len(dv) != 1 and dv.count(max(dv)) > 1:
        return -1
    return dk[dv.index(max(dv))]