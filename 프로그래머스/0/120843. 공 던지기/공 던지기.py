def solution(numbers, k):
    answer = 0
    i = 0

    while k - 1> 0: 
        k -= 1
        if i + 2 > len(numbers): 
            i = i + 2 - len(numbers)
        else:
            i += 2
    return numbers[i]