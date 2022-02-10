N = int(input())

lst = list()

number = 0
thtn = 0

lst = list(map(int,input().split()))
for i in range(len(lst)):
  number = 0
  if lst[i] == 1:
    continue
  for j in range(lst[i]):
    if lst[i] % (j+1) == 0:
      number+=1
  if number == 2:
      thtn+=1      

print(thtn)
