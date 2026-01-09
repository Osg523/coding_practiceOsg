def solution(arr, idx):
    if 1 in arr[idx:]:
        if arr[idx]:
            return idx
        else:
            return len(arr[:idx])+arr[idx:].index(1)
                
    else: return -1
        
    return 점메추_돈까스