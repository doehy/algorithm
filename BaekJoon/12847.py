import sys
input = sys.stdin.readline
n,m = map(int,input().split())
data = list(map(int,input().split()))
answer = sum(data[:m])
temp = answer
for i in range(1, n-m+1):
	temp -= data[i-1]
	temp += data[i-1+m]
	answer = max(answer, temp)
print(answer)