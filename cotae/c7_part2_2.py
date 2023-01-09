n = int(input())

data = list(map(int,input().split()))

data.sort()

m = int(input())

f_data = list(map(int,input().split()))

def check(data,target,start,end):
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return "yes"
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return "no"
    


for i in f_data:
    text = check(data,i,0,len(data)-1)
    print(text,end=' ')
