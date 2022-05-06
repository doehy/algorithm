import time
import random

start = time.time()

num_list= [32,512 , 128, 131072, 64, 524288, 2048, 32768, 8192, 16384,4096 , 65536,256 , 262144,1024 , 1048576]

num = len(num_list) 

for i in range(0,num-1):
    for j in range(i+1,num):
        if num_list[i] < num_list[j]:
            num_list[i],num_list[j] = num_list[j],num_list[i]

print(num_list)

print("time :", time.time()-start)
