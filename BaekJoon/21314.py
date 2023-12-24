text = input()

dp = [['0'] * len(text) for i in range(2)] 
big_temp = 0
small_temp = 0
k_flag = 0
flag = 0
# M이 중요해 최댓값은 m이 나타나고 k가 나타나기 전까지 쭉 가야하고 k에 대해서는 즉각 반응해야 해
# 최솟값은 m이 나타나고 다음 m이 나타날때까지 쭉 뻐겨야해 그리고 애도 k에 대해서는 즉각 반응
for i in range(len(text)):
    if text[i] == 'M':
        if k_flag == 1:
            big_temp = i
            small_temp = i
        else:
            big_temp = min(big_temp,i)
            small_temp = min(small_temp,i)
        if i == len(text) - 1:
            dp[0][big_temp:i+1] = '1' * (i-big_temp+1)
            dp[1][small_temp:i+1] = '1' + '0'*(i-small_temp)
        flag = 1
        k_flag = 0
    else: #문자가 k
        k_flag = 1
        if flag == 1: # M변수의 인덱스를 기록하고 있어
            dp[0][big_temp:i+1] = '5' + '0'*(i-big_temp)
            dp[1][small_temp:i] = '1' + '0'*(i-small_temp-1)
            dp[1][i] = '5'
        else:
            dp[0][i] = '5'
            dp[1][i] = '5'
        flag = 0    

print(''.join(dp[0]))
print(''.join(dp[1]))