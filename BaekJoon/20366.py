import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
data.sort()
result = float("inf")

for i in range(n-3):
    for j in range(i+3, n):
        left = i + 1
        right = j - 1
        while left < right:
            dif = (data[i] + data[j]) - (data[left] + data[right]) 
            if dif >= 0:
                result = min(result, abs(dif))
                left += 1
            else:
                result = min(result, abs(dif))
                right -= 1
print(result)