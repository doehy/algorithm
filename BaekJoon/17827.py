import sys
input = sys.stdin.readline

n,m,num = map(int,input().split())

data = list(map(int,input().split()))
pre_data = data[num-1:]
for i in range(m):
    go = int(input())
    if go < n: #입력이 노드의 개수보다 작은 경우
        print(data[go]) #그냥 돌 필요도 없으니 바로 출력
    else:
        go = go - n
        go = go % (n-num+1)
        print(pre_data[go])
        