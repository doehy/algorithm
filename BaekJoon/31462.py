import sys
input = sys.stdin.readline
n = int(input())
if n == 1:
    input()
    print(0)
else:
    check = []
    for i in range(n):
        check.append([0] * (i+1))
    data = []
    for _ in range(n):
        data.append(list(input().rstrip()))
    flag = 0
    for i in range(len(data)-1):
        for j in range(len(data[i])):
            if check[i][j]:
                continue
            if data[i][j] == 'R':
                if not check[i+1][j] and not check[i+1][j+1]:
                    if data[i+1][j] == 'R' and data[i+1][j+1] == 'R':
                        check[i][j] = check[i+1][j] = check[i+1][j+1] = 1
                    else:
                        flag = 1
                        break
                else:
                    flag = 1
                    break
            else:
                if j + 1 <= i:
                    if not check[i][j+1] and not check[i+1][j+1]:
                        if data[i][j+1] == 'B' and data[i+1][j+1] == 'B':
                            check[i][j] = check[i][j+1] = check[i+1][j+1] = 1
                        else:
                            flag = 1
                            break
                    else:
                        flag = 1
                        break
                else:
                    flag = 1
                    break
        if flag == 1:
            break

    if flag == 1:
        print(0)
    else:
        print(1)


# 일단 컬러별 개수로만 판단하는건 오바고
# 그리고 또한 뒤집혀 있는데 레드로 칠해져있거나 그 반대읙 경우도 안 됨
# 그러니까 이건 어떻게 판단해야 하냐면 흠..... 그냥 위에서부터 차근차근 내려와
# 그리고 r체크 밑에 두개있어 체크 그리고 바로 옆에 같은 경우는 b인 경우밖에 없어
# 그러니까 r이면 밑에가
# 줠라 수비네b이면 바로 밑에 다음 열이 b이면 된다.