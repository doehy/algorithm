import math

n = int(input())

tester = list(map(int,input().split()))

m_num , s_num = map(int,input().split())

result = 0

for i in tester:
    if m_num >= i:
        result += 1
    else:
        result += math.ceil((i-m_num) / s_num) +1 
print(result)