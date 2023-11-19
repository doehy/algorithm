def dfs():
    if len(s) == m: # m만큼 s가 찻다면 출력해 줄 것이다.
        print(' '.join(map(str,s))) #출력구문
        return #돌아가라
    for i in range(1,n+1): #1부터 n까지 숫자를 반복할 것이다. 왜? 순열을 구할라고
        if visited[i]: #방문한적이 있다면 밑으로 내려가지말고 다음 숫자로 넘어가라 왜? 중복순열이 아니기 때문에? 일단은
            continue
        visited[i] = True #방문한 적이 없다면 방문 처리를 해주고
        s.append(i) # s에 추가해준다.
        dfs() #m이랑 개수가 같은지 확인해주러간다.
        s.pop() #같다면 다음 반복을 위해서 pop을 해준다.
        visited[i] = False #


n,m = map(int,input().split())
visited = (n+1) * [False]
s = []

dfs()