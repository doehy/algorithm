n,m = map(int,input().split())
data = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)
# 반복문을 통해 0부터 주는 dfs
# 0으로 시작하는 dfs
# visited 때문에 가야하는데 못간다
# 그럼 그냥 set처리로 할까?
flag = 0
def dfs(num,count,temp): 
    global flag
    if flag == 1:
        return
    if count == 4:
        flag = 1
        return
    for node in data[num]:
        if node not in temp:
            temp.append(node)
            dfs(node,count+1,temp)
            temp.pop()

for i in range(n):
    temp = list()
    temp.append(i)
    dfs(i,0,temp)
    if flag == 1:
        print(1)
        break
if flag == 0:
    print(0)

# 문제에서 예를 든 것이 꼬리에 꼬리를 물고 있는 것이 4개 있었기에 예제 2번을 봤을 때 왜 1인지 몰랐다.
# 혹시 친구의 친구가 나와도 친구인 건가라는 생각이 들었지만 예제 3에서 아니라고 말을 해주었다.
# 그렇다면 왜 예제2는 1인거지? 여기서 한 번 반례를 생각을 하고 아니었으면 문제에서 이해한 것이 맞다고 생각을 하고
# 다시 처음으로 돌아와서 생각을 했어야 됐는데 머릿 속 로직이 꼬여서 혼자 예제를 만들기 시작했다.
# 결국 예제2만 이해하는데 약 1시간을 쏟았다. 
# 문제에서 이해한 것이 최대한 맞다고 생각을 하고 이상한 예제가 보이면 한 번 반례를 생각하고 아니면 다시 원래대로 돌아오는게 맞는 것 같다.

