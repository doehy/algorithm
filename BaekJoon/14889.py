import sys
input = sys.stdin.readline
n = int(input())

data = []

for i in range(n):
    data.append(list(map(int,input().split())))

s = []
nam_s = []
result = float("inf")

def score(data,s,nam_s):
    global result
    s_sum = 0
    nam_sum = 0
    for i in range(len(s)-1):
        for j in range(i,len(s)):
            s_sum += data[s[i]][s[j]] + data[s[j]][s[i]]
            nam_sum += data[nam_s[i]][nam_s[j]] + data[nam_s[j]][nam_s[i]]
    result = min(result,abs(s_sum - nam_sum))

def combi(data,num,s):
    if len(s) == num:
        nam_s = [] 
        for i in range(n):
            if i not in s:
                nam_s.append(i)
        score(data,s,nam_s)
        return
    else:
        if len(s) == 0:
            s.append(0)
            combi(data,num,s)
            s.pop()
        for i in range(n):
            if len(s) >= 1:
                if i > s[len(s)-1]:
                    s.append(i)
                    combi(data,num,s)
                    s.pop()
            
combi(data,n//2,s) # 여기서 사람수의 나누기 2로 인자값을 주는 이유는 인원 수의 반만 정해지면 나머지 반은 알아서 정해지기 때문이다.
print(result)