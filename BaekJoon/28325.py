N = int(input())
arr = list(map(int, input().split()))

def solve(arr):
    total = sum(arr)
    if total == 0:        
        return N // 2
    idx = 0
    for idx, a in enumerate(arr):
        if a:           
            break
    arr = arr[idx + 1:] + arr[:idx + 1]
    chk = [0] * N
    for i in range(N):
        if arr[i] or chk[i]:
            continue
        for j in range(i, N):
            if arr[j]:
                break
            chk[j] = 1
        total += (j - i + 1) // 2
    return total 

print(solve(arr))

