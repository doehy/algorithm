n = int(input())

text = input()
before = list(text)
count = 0
leng = 0
if len(text) % 2 == 0:
    leng = len(text) // 2 - 1
else:
    leng = len(text) // 2
while True:
    count += 1
    tp = ""
    for i in range(leng):
        tp += before[i] + before[-(i+1)]
    if len(text) % 2 == 0:
        tp += before[leng] + before[leng + 1]
    else:
        tp += before[leng]
    if tp == text:
        before = tp
        break
    before = tp

if n % count == 0:
    print(before)
else:
    before = list(text)
    for i in range(count - (n % count)):
        tp = ""
        for i in range(leng):
            tp += before[i] + before[-(i+1)]
        if len(text) % 2 == 0:
            tp += before[leng] + before[leng + 1]
        else:
            tp += before[leng]
        if tp == text:
            break
        before = tp
    print(before)
