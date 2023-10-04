w_score = list(map(int,input().split()))

g_score = list(map(int,input().split()))

i = 0
w_sum = 0
g_sum = 0

while i < 9:
    if i == 0:
        if w_score[i] > 0:
            print("Yes")
            break
    else:
        if w_sum+ w_score[i] > g_sum:
            print("Yes")
            break 

    w_sum += w_score[i]
    g_sum += g_score[i] 
    i += 1

if i == 9:
    print("No")