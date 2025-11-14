def solution(num, total):
    answer = []
    for i in range(-total-num, total+num):
        answer.append(i)
        if len(answer) == num:
            if sum(answer) == total:
                return answer
            else:
                del answer[0]
    return answer