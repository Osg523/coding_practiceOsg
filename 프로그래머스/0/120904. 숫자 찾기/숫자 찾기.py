def solution(num, k):
    answer = 0
    return str(num).find(str(k))+1 if str(num).find(str(k)) != -1 else -1