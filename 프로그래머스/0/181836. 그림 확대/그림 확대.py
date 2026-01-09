def solution(picture, k):
    answer = []
    for i in picture:
            answer += [''.join(j*k for j in i)]*k
    return answer