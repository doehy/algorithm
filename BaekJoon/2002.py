n = int(input())

i_data = dict()

for i in range(n):
    text = input()
    i_data[text] = i

o_data = []

for i in range(n):
    o_data.append(input())

result = 0
flag = 0
for i in range(n):
    for j in i_data.values():
        if j < i_data[o_data[i]]:
            result += 1 # 하나라도 있으면 결과 플러스 일을 해주고 사전에서도 없앤다. 그리고 반복문 빠져나오기
            del i_data[o_data[i]]
            flag = 1
            break
    if flag == 0:
        del i_data[o_data[i]]
    flag = 0    

print(result)
 