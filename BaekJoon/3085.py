n = int(input())

graph = []

for _ in range(n):
    graph.append(list(input()))

result = 0
max_result = 0
cmax_result = 0
temp_result = 0
max_temp_result = 0

def row_check(i,j,graph):
    number = 0
    max_number = 0
    graph[i][j],graph[i][j+1] = graph[i][j+1],graph[i][j] #값을 서로 바꿔준다.
    for p in range(n):
        if p+1 < n:
            if graph[i][p] == graph[i][p+1]:
                number += 1
            else:
                number = 0
            max_number = max(max_number,number)
    number = 0 #else를 들르지 않는다면 number가 0으로 초기화 되지 않기때문에 계속 증가한다.
    for k in range(j,j+2):
        for i in range(n):
            if i+1 < n:
                if graph[i][k] == graph[i+1][k]:
                    number += 1
                else:
                    number = 0
                max_number = max(max_number,number)
        number = 0
    graph[i][j],graph[i][j+1] = graph[i][j+1],graph[i][j]
    return max_number


def col_check(i,j,graph):
    number = 0
    max_number = 0
    graph[i][j],graph[i+1][j] = graph[i+1][j],graph[i][j] #값을 서로 바꿔준다.
    for p in range(n):
        if p+1 < n:
            if graph[p][j] == graph[p+1][j]:
                number += 1
            else:
                number = 0
            max_number = max(max_number,number)
    number = 0 #else를 들르지 않는다면 number가 0으로 초기화 되지 않기때문에 계속 증가한다.
    for k in range(i,i+2):
        for j in range(n):
            if j+1 < n:
                if graph[k][j] == graph[k][j+1]:
                    number += 1
                else:
                    number = 0
                max_number = max(max_number,number)
        number = 0
    graph[i][j],graph[i+1][j] = graph[i+1][j],graph[i][j]
    return max_number

# 가로를 먼저 확인해서 다른지를 확인하고 마지막에 세로를 확인해서 더 큰값을 출력하자.
for i in range(n):
    for j in range(n):
        z = graph[i][j]
        if j+1 < n:
            if z == graph[i][j+1]: #왼쪽 부분이 더 적은 경우에도 바꿨을 때 값은 끝까지 가기 때문에 그냥 else에서 브리크해서 계산해주면 된다.
                result += 1        #오른쪽 부분이 더 적은 경우에도 바꿨을 때는 값은 끝까지 가기 때문에 그냥 else에서 브리크해서 계산해주면 된다.
            else:
                temp_result = row_check(i,j,graph)
                max_temp_result = max(max_temp_result,temp_result)
    tt_result = max(result,max_temp_result) #계속 같을 때 값이 더 큰지 다를때 더 큰지 갱신하는 것이다.
    max_result = max(max_result,tt_result) #최종 max값을 갱신해나가는 것이다.
    result = 0 #result값이 계속 커지면 안되기 때문에 값을 초기화 해준다.
    temp_result = 0 #else를 안 들렀을 경우 전 값이 들어가있을 수 있기 때문에 0으로 초기화 해준다.


#세로로 확인을 한다.
for i in range(n):
    for j in range(n):
        z = graph[j][i]
        if j+1 < n:
            if z == graph[j+1][i]: 
                result += 1        
            else:
                temp_result = col_check(j,i,graph)
                max_temp_result = max(max_temp_result,temp_result)
    tt_result = max(result,max_temp_result) #계속 같을 때 값이 더 큰지 다를때 더 큰지 갱신하는 것이다.
    cmax_result = max(cmax_result,tt_result) #최종 max값을 갱신해나가는 것이다.
    result = 0 #result값이 계속 커지면 안되기 때문에 값을 초기화 해준다.
    temp_result = 0 #else를 안 들렀을 경우 전 값이 들어가있을 수 있기 때문에 0으로 초기화 해준다.

print(max(cmax_result,max_result)+1)