def solution(nums):
    answer = 0
    n = len(nums)
    for a in range(n-2):
        for b in range(a+1, n-1):
            for c in range(b+1, n):
                s = nums[a] + nums[b] + nums[c]
                if s > 1:
                    tf = True
                    for i in range(2,s):
                        if s % i == 0:
                            tf = False
                            break
                    if tf:
                        answer += 1
    return answer
