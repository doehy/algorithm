n = int(input())
data = list(map(int,input().split()))

data.sort(reverse=True)
cnt = 0
def check():
    global cnt
    for i in range(1,len(data)):
        if data[i] <= data[0]:
            cnt += data[i]
check()
if cnt >= data[0] - 1: # 제일 큰 수의 1차이나는것보다 크다면 어떻게 해서든 다 번갈아가면서 탈 수 있다.
    print(sum(data))
else:
    print(2 * cnt + 1)
