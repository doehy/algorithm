n = int(input())

graph = []

result = 0
max_result = 1

for _ in range(n):
    graph.append(list(input()))

dx = [1,0]
dy = [0,1]

for i in range(n):
    for j in range(n):
        temp_i = i
        temp_j = j
        while (j+1) < n:
            if graph[i][j] == graph[i][j+1]:
                max_result += 1
                j += 1
                result = max(result,max_result)
            else:
                j = temp_j
                max_result = 1
                break
            if j == (n -2):
                j = temp_j
                max_result = 1
        while (i+1) < n:
            if graph[i][j] == graph[i+1][j]:
                max_result += 1
                i += 1
                result = max(result,max_result)
            else:
                i = temp_i
                max_result = 1
                break
            if i == n-2:
                i = temp_i
                max_result = 1

for i in range(n):
    for j in range(n):
        temp_i = i
        temp_j = j #i,j가 3과 3이라고 가정하자
        for k in range(2):
            nx = i + dx[k] 
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n: #그래프안에 있고
                if graph[i][j] != graph[nx][ny]: #둘이 서로 다르면
                    if k == 0 : #밑으로 확인
                        graph[i][j],graph[nx][ny] = graph[nx][ny],graph[i][j]
                        for p in range(2):
                            max_result = 1
                            j = 0 # 0열부터 확인해야하니 0을 넣어놓는 것이다.
                            while (j+1) < n:
                                if graph[i+p][j] == graph[i+p][j+1]:
                                    max_result += 1
                                    j += 1
                                    result = max(result,max_result)
                                else:
                                    max_result = 1
                                    j += 1
                                    continue                                  
                        j = temp_j # 반복 끝났으면 j값에다가 원래 값 넣어놓기  
                        i = 0 
                        while (i+1) < n:
                            if graph[i][j] == graph[i+1][j]:
                                max_result += 1
                                i += 1
                                result = max(result,max_result)
                            else:    
                                i += 1
                                max_result = 1
                                continue
                        max_result = 1
                        i = temp_i 
                        graph[i][j],graph[nx][ny] = graph[nx][ny],graph[i][j] # 다시 제자리로 돌려준다.
                    if k == 1: #옆으로 확인
                        graph[i][j],graph[nx][ny] = graph[nx][ny],graph[i][j]
                        for p in range(2):
                            max_result = 1
                            i = 0 # 0열부터 확인해야하니 0을 넣어놓는 것이다.
                            while (i+1) < n:
                                if graph[i][j+p] == graph[i+1][j+p]:
                                    max_result += 1
                                    i += 1
                                    result = max(result,max_result)
                                else:
                                    max_result = 1
                                    i += 1
                                    continue
                        i = temp_i # 반복 끝났으면 i값에다가 원래 값 넣어놓기
                        j = 0   
                        while (j+1) < n:
                            if graph[i][j] == graph[i][j+1]:
                                max_result += 1
                                j += 1
                                result = max(result,max_result)
                            else:    
                                max_result = 1
                                j += 1
                                continue
                        j = temp_j
                        graph[i][j],graph[nx][ny] = graph[nx][ny],graph[i][j]
                        max_result = 1



print(result)



