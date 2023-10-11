import sys
input = sys.stdin.readline
n,m,p = map(int,input().split())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))

def solve():
    global p
    for i in range(n):
        cnt = 0
        data[i].sort()
        for num in data[i]:
            if num == -1:
                cnt += 1
                continue
            else:
                if p >= num:
                    p += num
                else:
                    while cnt > 0:
                        p *= 2
                        cnt -= 1
                        if p >= num:
                            break
                    if p >= num:
                        p += num
                    else:
                        return 0  
        p *= (2 ** cnt)                    
    return 1               

print(solve())