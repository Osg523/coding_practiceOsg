def solution(num_list):
    a = 1 
    if len(num_list) < 11:
        for i in num_list:
            a*=i 
    else: return sum(num_list)
    return a