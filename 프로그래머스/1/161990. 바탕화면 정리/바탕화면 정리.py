def solution(wallpaper):
    n = []
    nx = []
    ny = []
    a, b = 0, 0
    for i in wallpaper:
        a = 0
        for j in i:
            if j == "#":
                n.append([a,b])
            a += 1
        b += 1
    for i, j in n:
        nx.append(i)
        ny.append(j)
    answer = [min(ny), min(nx), max(ny)+1, max(nx)+1]
    return answer