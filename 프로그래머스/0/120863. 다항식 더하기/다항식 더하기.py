def solution(polynomial):
    x = 0
    c = 0
    for i in polynomial.replace('+',"").split():
        if 'x' in i:
            if len(i) == 1:
                x += 1
            else:
                x += int(i[:-1])
        else:
            c += int(i)
    return (f'{x}x' if x > 1 else 'x') + (f' + {c}' if c > 0 else '') if x > 0 else f'{c}'