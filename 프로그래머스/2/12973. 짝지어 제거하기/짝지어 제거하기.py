def solution(s):
    answer = -1
    a = 0
    list1 = []
    for i in s:
        list1.append(i)
        if len(list1) > 1 and list1[a-1] == list1[a]:
            list1.pop()
            list1.pop()
            a -= 2
        a += 1
    
    if len(list1) == 0:
        answer = 1
    else:
        answer = 0
        
    return answer