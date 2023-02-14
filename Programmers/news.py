str1, str2 = input().split()

if len(str1) == 0 and len(str2) == 0:
    print(0)
else:
    one_li = []
    two_li = []

    for i in range(len(str1)-1):
        if (str1[i] + str1[i+1]).isalpha():
            one_li.append(str1[i].upper() + str1[i+1].upper())

    for i in range(len(str2)-1):
        if (str2[i] + str2[i+1]).isalpha():
            two_li.append(str2[i].upper() + str2[i+1].upper())

    and_li = 0
    or_li = 0

    for i in set(one_li): #중복하지 않기 위해서 집합인 상태에서 반복한다.
        if i in set(two_li): #많은 반복을 하지 않기 위해 애도 집합 처리를 해준다. 
            or_li += max(one_li.count(i),two_li.count(i))
            and_li += min(one_li.count(i),two_li.count(i))
        else:
            or_li += one_li.count(i)

    for i in set(two_li):
        if i not in set(one_li):
            or_li += two_li.count(i)

    if and_li == 0:
        print(0)
    elif or_li == 0:
        print(0)
    else:
        print(int(and_li / or_li * 65536))

