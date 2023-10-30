k=int(input())
c=int(input())
ans=[]
for i in range(c):
    m,n=map(int,input().split())
    if m<n: # 동수가 더 클경우
        if n-m-1>=k-n+1: ans.append("0")
        else: ans.append("1")
    elif m>n: # 영희가 더 클 경우
        if m-n-1>k-m+1: ans.append("0")
        else: ans.append("1")
    else: ans.append("1")
for i in ans: print(i)