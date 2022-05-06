import time

start = time.time()

num_list= [32,512 , 128, 131072, 64, 524288, 2048, 32768, 8192, 16384,4096 , 65536,256 , 262144,1024 , 1048576]
def shell_sort(arr):
    N = len(arr)
    h = N // 2
    while h > 0:
        for i in range(h, N):
            temp = arr[i]
            j = i - h
            while j >= 0 and arr[j] > temp:
                arr[j + h] = arr[j]
                j -= h
            arr[j + h] = temp
        h //= 2
 
    print(num_list)
 
shell_sort(num_list)
print("time :", time.time()-start)
