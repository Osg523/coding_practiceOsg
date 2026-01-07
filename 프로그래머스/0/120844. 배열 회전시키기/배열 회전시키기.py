def solution(numbers, direction):
    answer = []
    if direction == 'left':
        a = numbers[0]
        for i in range(0,len(numbers)-2):
            numbers[i],numbers[i+1] = numbers[i+1],numbers[i+2]
        numbers[-1] = a
    else:
        a = numbers[-1]
        for i in range(len(numbers)-1,0,-1):
            numbers[i],numbers[i-1] = numbers[i-1],numbers[i-2]
        numbers[0] = a
    return numbers