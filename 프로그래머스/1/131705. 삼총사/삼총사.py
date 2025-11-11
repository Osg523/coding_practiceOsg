def solution(number):
    answer = 0
    n = -1
    for a in range(0, len(number)-2):
        for b in range(a+1,len(number)-1):
            for c in range(b+1,len(number)):
                n = number[a]+number[b]+number[c]
                if n == 0:
                    answer += 1
    return answer