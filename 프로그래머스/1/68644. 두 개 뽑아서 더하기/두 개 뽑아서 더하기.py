def solution(numbers):
    answer = []
    for i in numbers:
        idx=numbers.index(i)
        del(numbers[idx])
        for j in numbers:
            answer.append(i + j)
        numbers.insert(idx,i)
    b = set(answer)
    b = sorted(list(b))
    return b