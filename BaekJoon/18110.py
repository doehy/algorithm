import sys
input = sys.stdin.readline

def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)
n = int(input())
if n == 0:
    print(0)
else:
    data = list(int(input()) for _ in range(n))
    answer = 0
    ran = round2(n / 100 * 15)
    data.sort()
    answer = round2(sum(data[ran:n-ran]) / (n - 2*ran))
    print(answer)
