def solution(s, skip, index):
    answer = ''
    a = [ord(i) for i in s]
    b = [ord(i) for i in skip]
    for i in a:
        for j in range(index):
            i += 1
            if i > ord('z'):
                i = ord('a')
            while i in b:
                i += 1
                if i > ord('z'):
                    i = ord('a')
        answer += chr(i)
                
    return answer