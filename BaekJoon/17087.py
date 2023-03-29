n,s = map(int,input().split())

data = list(map(int,input().split()))

def gcd(x,y):
    while x % y != 0:
        x,y = y, x % y
    return y

result = float("inf")

se = set()

for i in data:
    se.add(abs(s-i))

li = list(se)
li.sort()
temp = li[0]

for i in li:
    result = min(result, gcd(i,temp))
    temp = result

print(result)
