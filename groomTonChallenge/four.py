import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
maxNum = max(data)
idx = data.index(maxNum)
flag = 0
for i in range(idx-1,-1,-1):
	if data[i+1] < data[i]:
		flag = 1	
		break
if flag == 0:
	for i in range(idx+1, len(data)):
		if data[i-1] < data[i]:
			flag = 1
			break
if flag == 0:
	print(sum(data))
else:
	print(0)