def solution(arr):
    if ''.join(map(str,arr)).find('2') != -1:
        first, last = arr.index(2),0
        for i,j in enumerate(arr):
            if j == 2:
                last = i
        return arr[first:last+1]
    else:
        return [-1]
    return arr[first:last+1]