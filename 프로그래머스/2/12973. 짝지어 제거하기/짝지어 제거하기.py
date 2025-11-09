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
    
''' pop함수 없이
def solution(s):

    answer = 0
    a = list(s)
    top = -1
    i = 0

    while i < len(a):
        if top >= 0 and a[top] == a[i]:
            top -= 1
        else:
            top += 1
            a[top] = a[i]
        i += 1
    if top == -1:
        answer = 1

    return answer
'''
''' 시간복잡도 O(n^2)이라 정확도는 맞지만 del함수 원인으로 효율성 부분에서 실패함
def solution(s):
    answer = 0
    a = list(s)
    i = 1
    while i < len(a):
        if a[i] == a[i-1]:
            del a[i-1:i+1]
            if i > 1:
                i -= 1
        else:
            i += 1
    if a == []:
        answer = 1
    return answer
'''
