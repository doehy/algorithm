n = int(input())

num_list= []

for _ in range(n):
    num_list.append(int(input()))

num = len(num_list)

for i in range(0,num-1):
    for j in range(i+1,num):
        if num_list[i] < num_list[j]:
            print(num_list[j])
            num_list[i],num_list[j] = num_list[j],num_list[i]

print(num_list)