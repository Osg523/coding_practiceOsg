def solution(my_string):
    for i in my_string:
        if i >= 'A':
            my_string = my_string.replace(i," ")
    answer = sum(int(i) for i in my_string.split())
    return answer