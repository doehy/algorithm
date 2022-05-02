N = int(input())

lst = input().split()

r=1
c=1

for i in lst:
    if i == "L" and c != 1:
        c -= 1
    elif i == "L" and c == 1:
        continue
    if i == "R" and c != 5:
        c += 1
    elif i == "R" and c == 5:
        continue
    if i == "U" and r != 1:
        r -= 1
    elif i == "U" and r == 1: 
        continue
    if i == "D" and r != 5:
        r += 1
    elif i == "D" and r == 5:
        continue

print(r, c)