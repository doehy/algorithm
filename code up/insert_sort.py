import time

num_list= [32,512 , 128, 131072, 64, 524288, 2048, 32768, 8192, 16384,4096 , 65536,256 , 262144,1024 , 1048576]
num = len(num_list)

start = time.time()
for i in range(1,num):
    for j in range(i,0,-1): #end+1까지 감소한다.
        if num_list[j] < num_list[j-1]:
            num_list[j],num_list[j-1] = num_list[j-1],num_list[j]
        else:
            break
print(num_list)
print("time :", time.time()-start)