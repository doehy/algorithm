from collections import defaultdict
around = input()
cow = defaultdict(list)
visited = set()
for i in range(len(around)):
	if around[i] not in visited:
		visited.add(around[i])
	else:
		visited.discard(around[i])
	for temp in visited:
		if temp != around[i]:
			if around[i] not in cow[temp]:
				cow[temp].append(around[i])
			else:
				cow[temp].remove(around[i])

answer = 0
ans = set()
for x,y in cow.items():
	for z in y:
		if (x,z) not in ans and (z,x) not in ans:
			ans.add((x,z))
			ans.add((z,x))
			answer += 1
print(answer)

# 또 하나의 방법
# text = input()
# pos1 = [0] * 26
# pos2 = [0] * 26
# answer = 0
# for i in range(52):
# 	tp = ord(text[i]) - 65
# 	if pos1[tp] == 0:
# 		pos1[tp] = i + 1
# 	else:
# 		pos2[tp] = i + 1

# for i in range(26):
# 	for j in range(26):
# 		if pos1[i] < pos1[j] and pos1[j] < pos2[i] and pos2[i] < pos2[j]:
# 			answer += 1

# print(answer)