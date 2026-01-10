def solution(order):
    return sum(4500 if 'cafelatte' not in i else 5000 for i in order)

'''
def solution(order):
    answer = 0
        for i in order:
            if 'cafelatte' not in i:
                answer += 4500
            else:
                answer += 5000
    return answer
'''