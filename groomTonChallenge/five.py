import sys
input = sys.stdin.readline
n,k = map(int,input().split())
data = list(map(int,input().split()))
result = []
def check(number):
	count = 0
	while number != 0:
		if number % 2 == 1:
			count += 1
		number //= 2
	return count

for num in data:
	tp = check(num)
	result.append([tp,num])

result = sorted(result, key=lambda x:[-x[0],-x[1]])
print(result[k-1][1])