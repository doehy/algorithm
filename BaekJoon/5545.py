n = int(input())
a,b = map(int,input().split())
dow = int(input())
data = []
for i in range(n):
    data.append(int(input()))
data.sort(reverse=True)
money = a
kalori = dow
won = dow / a

for i in data:
    money += b
    kalori += i
    now = kalori / money
    if won < now:
        won = now
    else:
        break

print(int(won))