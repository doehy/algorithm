import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m = int(input())
    answer = [[0,0]]
    dic = dict()
    for i in range(m):
        x,y = map(int,input().split())
        if x not in dic:
            dic[x] = []
        dic[x].append(y)
    sdic = sorted(dic.items())
    for j in range(len(sdic)):
        sdic[j][1].sort()
        if answer[-1][1] != sdic[j][1][0]:
            sdic[j][1].sort(reverse = True)
        for k in range(len(sdic[j][1])):
            answer.append([sdic[j][0], sdic[j][1][k]])
    que = list(map(int,input().split()))
    for i in range(1,len(que)):
        print(*answer[que[i]])
    
# 테스트 케이스는 몇 개 일지도 모르고 매번 테케마다 최대 카페는 십만 개일 수 있다.
# 이 때 정렬은 아주 매우 간단하게 해야한다.
