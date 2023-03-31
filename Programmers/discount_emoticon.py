def check(s,emoticons,discount,users,lis):
    if len(s) == len(emoticons):
        count = 0; total = 0
        for dis,money in users:
            temp = 0
            for i in range(len(s)):
                if s[i] >= dis: # 할인율이 dis보다 많다면
                    temp += emoticons[i] * (100 - s[i]) // 100
            if money <= temp:
                count += 1
            else:
                total += temp
        lis.append((count,total))
        return
    if len(s) == 0:
        for i in range(len(discount)):
            s.append(discount[i])
            check(s,emoticons,discount,users,lis)
            s.pop()
    for i in range(len(discount)):
        s.append(discount[i])
        check(s,emoticons, discount,users,lis)
        s.pop()

def solution(users, emoticons):
    answer = []
    discount = [40,30,20,10]
    lis = list()
    s = []
    check(s,emoticons,discount,users,lis)
    lis = sorted(lis, key = lambda x : (-x[0],-x[1]))
    answer.append(lis[0][0])
    answer.append(lis[0][1])
    return answer

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600,4900]
print(solution(users, emoticons))
