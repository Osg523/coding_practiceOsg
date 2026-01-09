def solution(my_string, indices):
    answer = list(my_string)
    for i,j in enumerate(sorted(indices)):
        del answer[j-i]
    return ''.join(answer)