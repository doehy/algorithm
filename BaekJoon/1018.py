n,m = map(int,input().split())

data = [list(input()) for _ in range(n)]

min_result = float("inf")

def check(x,y,color):
    idx1 = 0
    idx2 = 0
    for i in range(x,x+8):
        for j in range(y,y+8):
            if(i+j) % 2 == 0:
                if data[i][j] != 'W':
                    idx1 += 1
                if data[i][j] != 'B':
                    idx2 += 1
            else:
                if data[i][j] != 'B':
                    idx1 += 1
                if data[i][j] != 'W':
                    idx2 += 1
            
    return min(idx1,idx2)

for i in range(n+1-8):
    for j in range(m+1-8):
        min_result = min(min_result,check(i,j,data[i][j]))

print(min_result)
