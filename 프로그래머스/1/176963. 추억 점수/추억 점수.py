def solution(name, yearning, photo):
    answer = []
    for i in photo:
        s = 0
        for j in i:
            if j in name:
                s += yearning[name.index(j)]
        answer.append(s)
    return answer