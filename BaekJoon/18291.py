import sys
input = sys.stdin.readline
t = int(input())
modNum = 10 ** 9 + 7
def solve(a,b,m): # 2 8
    ret = 1
    while b > 0:
        if b % 2:
            ret = ret * a % m
        b //= 2
        a = (a*a) % m  
    return ret

for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
    else:
        print(solve(2,n-2,modNum))