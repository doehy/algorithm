a,b = map(int,input().split())

m = int(input())

number = list(map(int,input().split()))

a_sum = 0

for i in range(m):
    a_sum += number[i] * (a**(m-1))
    m -= 1

b_number = []

while (a_sum != 0):
    pr = a_sum % b
    b_number.append(pr)
    a_sum //= b

b_number.reverse()
for i in b_number:
    print(i,end=' ')





