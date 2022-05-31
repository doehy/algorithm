n = int(input())

data = list(input())

result = 0

text = data[0]

num = len(data)
num -= 1

while num > 0 :
    if data[num] == text:
        break
    else:
        num -= 1
        continue

number = 1

while number < num:
    if data[number] != text:
        result += 1
        while data[number] != text:
            number += 1
    else:
        number+=1

if num+1 == len(data):
    print(result+1)
else:
    print(result+2)

