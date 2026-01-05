def solution(my_strings, parts):
    return ''.join(j[parts[i][0]:parts[i][1]+1] for i,j in enumerate(my_strings))