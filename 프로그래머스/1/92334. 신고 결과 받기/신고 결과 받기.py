def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    count = dict()
    ban_list = []

    for i in set(report):
        j = i.split(" ")
        if j[1] in count:
            count[j[1]] += 1
        else:
            count[j[1]] = 1

    for key, v in count.items():
        if v >= k:
            ban_list.append(key)
    
    for i in set(report):
        j = i.split(" ")
        if j[1] in ban_list:
            answer[id_list.index(j[0])] += 1
        
    return answer