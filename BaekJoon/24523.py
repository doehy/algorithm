# 27649
import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
re = [0] * n
re[-1] = -1
for i in range(n-2,-1,-1):
    if data[i] == data[i+1]:
        re[i] = re[i+1]
    else:
        re[i] = i + 2
print(*re) 



# n의 크기는 최대 백만, 자신보다 뒤에 있는 값중 가장 작은 최솟 값을 찾아야 한다.