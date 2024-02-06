import sys
input = sys.stdin.readline
n = int(input())
voca = []
for _ in range(n):
    voca.append(input().rstrip())

vocaDict = dict()
ans = [0,0,0]
for i in range(len(voca)):
    temp = ''
    for j in range(len(voca[i])):
        temp += voca[i][j]
        if temp not in vocaDict:
            vocaDict[temp] = [i, len(temp)]
        else: # 현재 문자열이 사전에 있어
            if ans[0] < len(temp):
                ans = [len(temp), vocaDict[temp][0], i]
            elif ans[0] == len(temp):
                if ans[1] > vocaDict[temp][0]:
                    ans = [len(temp), vocaDict[temp][0], i]
                
print(voca[ans[1]])
print(voca[ans[2]])
