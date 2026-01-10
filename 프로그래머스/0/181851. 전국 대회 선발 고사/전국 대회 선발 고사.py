def solution(rank, attendance):
    answer = sorted([rank[i] for i, j in enumerate(attendance) if j])       
    return rank.index(answer[0])*10000+rank.index(answer[1])*100+rank.index(answer[2])