N = int(input())
S = map(int, input().split())
sum = 0; cnt = 0
for x in S:
	sum += x
	cnt += x // 2
print("YES" if sum % 3 == 0 and cnt >= sum // 3 else "NO")


# data의 최대 길이는 십만이고 물을 주는 경우가 1,2 아니면 3이다. 근데 이걸 하나하나 다 빼볼 수도 없는 노릇
# 다 빼볼 시 시간초과가 나온다. 그렇다면 뭘까
# 여기서 총합이 3으로 나누어 떨어져야 한다는 첫번째 조건을 누구나 할 수 있는 생각
# 여기서 총합이 3으로 나눈 몫보다 각 데이터의 2를 최대한 몇개 닮을 수 있었는지에 대해 cnt >= sum // 3
# 왜 저 값이 성립이 될까 sum // 3을 하면 필요한 일 수가 나온다 즉 2를 최대한 몇번 뿌릴 수가 있는지 나온다.
# 1 3 1 3 1인 경우 2를 최대 3번 뿌려야 한다. 그러나 2는 최대 2번 밖에 뿌릴 수가 없다. 고로 저것은 만들지 못하낟.
# 여기서 나는 각 모든 수가 2 또는 3으로 나눠줘야 한다고 생각을 했다. 그래야마나 동작을 할 것이라고 믿었다.
# 그러나 4,5인 경우도 "yes"가 나오기 때문에 틀린 가정이다. 


