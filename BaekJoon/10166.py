from math import gcd
def solve():
    s,e = map(int,input().split())
    arr = [[0] * (e) for _ in range(e)]
    answer = 0
    for i in range(s,e+1):
        for j in range(1,i+1):
            num = gcd(i,j)
            x,y = i //num , j //num
            if not arr[x-1][y-1]:
                arr[x-1][y-1] = 1
                answer += 1
            
    print(answer)

solve()