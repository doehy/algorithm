n = int(input())
dic = dict()
for i in range(n):
    text = input()
    for i in range(len(text)):
        if text[i] not in dic:
            dic[text[i]] = 10 ** (len(text)-1 - i)
        else:
            dic[text[i]] += 10 ** (len(text)-1 - i)

answer = list(dic.values())
answer.sort(reverse=True)
num = 9
total = 0
for i in answer:
    total += i * num
    num -= 1
print(total)
