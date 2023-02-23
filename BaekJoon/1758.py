import sys 
input = sys.stdin.readline

N = int(input())

data = []

for i in range(N):
    data.append(int(input()))
    data.sort(reverse=True)

count = 0
for i in range(N):
    if data[i] - i > 0:
        count += data[i] - i

print(count)
# 각자 줄 금액을 정해놨고, 자기 index를 자기가 줄라했던 돈에서 빼면 된다.
# 나는 최대한 많이 받고 싶은건데 흠... 음수가 되면 돈을 못받아
# 최대한 못받는 경우를 만들어봤는데 걍 많이 주는놈을 제일 앞에 세우는게 짱이야
#  