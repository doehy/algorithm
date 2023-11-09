n,m = map(int,input().split())

data = list(map(int,input().split()))

p_data = list(map(int,input().split()))

data.extend(p_data)
data.sort()
data = list(map(str,data))

print(' '.join(data))
