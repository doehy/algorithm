import sys  
sys.stdin = open('input.txt')  
input = sys.stdin.readline  
  
N, M = map(int, input().split())  
K = int(input())  
mod = 10**9+7  
# N번 행까지 사용해야되므로 덧셈시 조건을 줄이기 위해 한줄 더 생성  
bee_house = [[0]*(M+1) for _ in range(N+2)]  
# 시작점도 구멍으로 쳐주어서 0으로 초기화 안되게 하기  
hole = {(1,1)}  
for _ in range(K):  
    a, b = map(int, input().split())  
    # 구멍칸 넣어주기  
    hole.add((a,b))  
  
  
bee_house[1][1] = 1  
  
# 1행, 1열은 채웠으므로  
# 2행 2열부터 시작  
# 이 때 열부터가 아닌, 행부터 채워주어야 한다.  
for j in range(1,M+1):  
    for i in range(1,N+1):  
  
        # 구멍칸 통과  
        if (i,j) in hole:  
            continue  
        # 짝수 열 기록  
        elif not j % 2:  
            # 왼쪽 아래 조건 없애기 위해서 1행 더 추가해줌  
            bee_house[i][j] = (bee_house[i-1][j] + bee_house[i][j-1] + bee_house[i+1][j-1]) % mod  
        # 홀수 열 기록  
        else:  
            # 홀수 열의 경우 덧셈해주는 칸이 모두 범위 내부임  
            bee_house[i][j] = (bee_house[i-1][j] + bee_house[i][j-1] + bee_house[i-1][j-1]) % mod  
print(bee_house[N][M])