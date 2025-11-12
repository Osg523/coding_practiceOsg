def solution(spell, dic):
    answer = 2
    for i in dic:
        a = 0
        for j in spell:
            if i.count(j) == 1:
                a += 1
        if a == len(spell):
            answer = 1
    return answer

'''
def solution(spell, dic):
    answer = 2
    a = 0
    for i in dic:
        for j in spell:
            if j in i:
                a += 1
        if a == len(spell):
            answer = 1
        a = 0
    return answer
이 코드도 통과됩니다.
문제에서는 spell에 포함된 리스트 요소를 각각 한 번씩만 사용해 단어를 만들 수 있을 때 1을 반환해야 합니다.
하지만 반례로 ["z", "d", "x"], ["ddxxzz"]를 입력하면 2가 반환되어야 합니다.
따라서 이 코드는 통과되지 않아야 한다고 생각됩니다.
즉, “한 번씩만”이라는 조건이 단어가 여러 번 만들어지는 경우(2개 이상)까지 허용되는 의미인지 궁금합니다.
'''
'''
라고 건의함 
건의 결과는 나중에 작성
'''
