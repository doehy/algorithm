c = int(input())

def solve(s,t,count):
    global answer
    if s > t:
        return
    if s == t:
        answer = min(answer,count)        
        return    
    solve(s*2,t+3,count+1)
    solve(s+1,t,count+1)



for i in range(c):
    answer = float("inf")
    s,t = map(int,input().split())
    solve(s,t,0)
    print(answer)

# 백트래킹 문제 같은데