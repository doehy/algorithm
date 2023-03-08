text = list(input())

stack = []
temp = ""
accrue = 0

for c in text:
    if c.isdigit():
        accrue += 1
        temp = c
    elif c == "(":
        stack.append((temp, accrue - 1))
        accrue = 0
    else:
        multi, preL = stack.pop()
        accrue = (int(multi) * accrue) + preL

print(accrue)