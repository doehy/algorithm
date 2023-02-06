k = int(input())
text = input().split()
# 시간복잡도를 위해 수열 두개를 만들고 함수도 두개를 쓴다
max_stor = [str(i) for i in range(9,9-(k+1),-1)]
min_stor = [str(i) for i in range(0,k+1)]

max_num = 0
min_num = float("inf")

def check_max(idx,s):
    global max_num
    if len(s) == k+1:
        flag = 0
        for i in range(k):
            if text[i] == '<' and int(s[i]) < int(s[i+1]):
                continue
            elif text[i] == '>' and int(s[i]) > int(s[i+1]):
                continue
            else: # 위에 두 조건을 만족하지 않아
                flag = 1
                break
        if flag == 0:
            max_num = max(max_num,''.join(s))
        return
    s.append(max_stor[idx]) # 현재 인덱스를 추가하거나
    check_max(idx+1,s) 
    s.pop() # 현재 인덱스를 없애거나
    check_max(idx+1,s)
    
def check_min(idx,s):
    global min_num
    if len(s) == k+1:
        flag = 0
        for i in range(k):
            if text[i] == '<' and int(s[i]) < int(s[i+1]):
                continue
            elif text[i] == '>' and int(s[i]) > int(s[i+1]):
                continue
            else: # 위에 두 조건을 만족하지 않아
                flag = 1
                break
        if flag == 0:
            min_num = min(min_num,''.join(s))
        return
    s.append(min_stor[idx]) # 현재 인덱스를 추가하거나
    check_max(idx+1,s) 
    s.pop() # 현재 인덱스를 없애거나
    check_max(idx+1,s)
    
s = []
check_max(0,s)
s = []
check_min(0,s)

print(*max_num)
print(*min_num)

