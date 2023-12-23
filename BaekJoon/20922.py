n,k = map(int,input().split())
data = list(map(int,input().split()))
left, right = 0, 1
dic = dict()
max_num = 0
if n == 1:
    print(1)
else:
    dic[data[left]] = 1
    while right < len(data):
        if data[right] not in dic:
            dic[data[right]] = 1
        else:
            dic[data[right]] += 1
            if dic[data[right]] > k: # k와 같을 경우
                max_num = max(max_num, right - left)
                while dic[data[right]] > k:
                    dic[data[left]] -= 1
                    left += 1
        right += 1
    max_num = max(max_num,right - left)
    print(max_num)