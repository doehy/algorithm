text = list(input())

left,right = 0, len(text) - 1

flag = 0
while left <= right: # 같은 경우까지 봐줘야 한다. 문자열 길이가 홀수일 수도 있을 수 있기 때문에
    if text[left] != text[right]:
        flag = 1
        break
    left += 1
    right -= 1

t_flag = 0
if flag == 0:
    for i in range(len(text)-1):
        if text[i] != text[i+1]:
            t_flag = 1
            break
    if t_flag == 0:
        print(-1)
    else:
        print(len(text) - 1)
else:
    print(len(text))