def solution(nums):
    answer = 0
    numset = set(nums)
    n = len(nums) // 2
    if n < len(numset):
        answer = n
    else:
        answer = len(numset)
    return answer