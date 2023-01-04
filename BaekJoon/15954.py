n,k = map(int,input().split())

data = list(map(int,input().split()))
result = float("INF")

def avg(temp):
    m = sum(temp) / len(temp) # 평균
    sdminus(m,temp)

def sdminus(m,temp): # 표준편차
    global result
    count = 0
    for i in temp:
        count += (i-m) ** 2
    sd = (count / len(temp)) ** 0.5 
    result = min(result,sd)

for i in range(n-k+1): #0,1,2
    for j in range(k,n-i+1):
        temp = data[i:i+j] 
        avg(temp)
        

print(result)