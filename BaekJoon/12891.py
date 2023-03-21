s,p = map(int,input().split())
text = list(input())
A,C,G,T = map(int,input().split())
a_num, c_num, g_num, t_num = 0, 0, 0, 0
answer = 0
for i in range(p):
    if text[i] == 'A':
        a_num += 1
    elif text[i] == 'C':
        c_num += 1
    elif text[i] == 'G':
        g_num += 1
    else:
        t_num += 1

if a_num >= A and c_num >= C and g_num >= G and t_num >= T:
    answer += 1

left, right = 0, p

for i in range(p,s):
    if text[left] == 'A':
        a_num -= 1
    elif text[left] == 'C':
        c_num -= 1
    elif text[left] == 'G':
        g_num -= 1
    else:
        t_num -= 1
    if text[right] == 'A':
        a_num += 1
    elif text[right] == 'C':
        c_num += 1
    elif text[right] == 'G':
        g_num += 1
    else:
        t_num += 1
    if a_num >= A and c_num >= C and g_num >= G and t_num >= T:
        answer += 1
    left += 1
    right += 1
    print(i,a_num,c_num,g_num,t_num)
print(answer)

# 문자열의 길이가 최대 백만이다. 
# 매번 모든 경우를 탐색한다면 무조건 시간초과가 발생한다.
# 투 포인터 적으로 접근해보자