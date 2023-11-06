import sys
input = sys.stdin.readline
text = input().rstrip()
num = 0
wolf = ['o','l','f']
def findNum(num, pro):
    cnt = 0
    for i in range(num, len(pro)):
        if pro[i] == 'w':
            cnt += 1
        else:
            break
    return cnt

def isCorrect(idx,cnt, num, pro):
    count = 0
    for i in range(num, len(pro)):
        if pro[i] == wolf[idx]:
            count += 1
        else:
            break
    if cnt == count:
        return 1
    else:
        return 0

def solve(pro):
    global num
    cnt = findNum(num, pro)
    if cnt == len(pro) or cnt == 0 or cnt > len(pro) // 4:
        return 0
    num += cnt
    if isCorrect(0,cnt,num,pro) == 0:
        return 0
    num += cnt
    if isCorrect(1,cnt,num,pro) == 0:
        return 0
    num += cnt
    if isCorrect(2,cnt,num,pro) == 0:
        return 0
    num += cnt
    if num < len(pro):
        return solve(pro)
    else:
        return 1

print(solve(text))
