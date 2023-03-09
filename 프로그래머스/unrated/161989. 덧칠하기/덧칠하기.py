def solution(n, m, section):
    answer = 0
    visited = [0] * (n+1)
    for i in section:
        if visited[i]:
            continue
        answer += 1
        for j in range(i,i+m):
            if j > n:
                break
            visited[j] = 1
    return answer