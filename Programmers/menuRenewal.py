def solution(orders, course):
    answer = []
    def check(order, num,s):
        if len(s) == num:
            lis.append(''.join(s))
            return
        if len(s) == 0:
            for i in range(len(order)):
                s.append(order[i])
                check(order, num, s)
                s.pop()
        else:
            for i in range(len(order)):
                if order[i] > s[-1]:
                    s.append(order[i])
                    check(order, num, s)
                    s.pop()

    for num in course:
        dic = dict()
        lis = list() 
        for order in orders:
            if num > len(order):
                continue 
            check(order, num,[])
        for text in lis:
            if text not in dic:
                dic[text] = 1
            else:
               dic[text] += 1
        if len(dic) < 1:
            continue
        max_num = max(dic.values())
        if max_num < 2:
            continue
        for tx,val in dic.items():
            if val == max_num:
                answer.append(tx)
    answer.sort()
    return answer