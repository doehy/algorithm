n,m = map(int,input().split())
s = list(input())
t = list(input())
snum = tnum = 0
s_data = []
t_data = []
for num in range(len(s)):
    if s[num] == '1':
        s_data.append(num)
    if t[num] == '1':
        t_data.append(num)

answer = 0
for i in range(len(s_data)):
    answer += abs(s_data[i] - t_data[i])
re = 0
if answer % 2 == 0:
    re = (answer // 2) ** 2 * 2
else:
    re = (answer // 2) ** 2
    re += (answer // 2 + 1) ** 2
print(re)