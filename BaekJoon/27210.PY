n = int(input())

data = list(map(int,input().split()))

l_answer = 0
r_answer = 0
answer = 0

def l_check():
    total = 0
    tp = 0
    for i in data:
        if i == 1:
            total += 1
            tp = max(tp,total)
        else:
            if total != 0:
                total -= 1
            else:
                pass
    return tp

def r_check():
        total = 0
        tp = 0
        for i in data:
            if i == 2:
                total += 1
                tp = max(tp,total)
            else:
                if total != 0:
                    total -= 1
                else:
                    pass
        return tp



l_answer = l_check()
r_answer = r_check()
answer = max(l_answer,r_answer)
print(answer)

# 결국 둘의 차이가 최대일 때가 정답인데 