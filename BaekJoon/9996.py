n = int(input())
pattern = input() # 나중에 비교를 하기 위해서 문자열로 남겨둔다.
temp = list(pattern) # 나중에 쓸 수 도 있으니 일단 리스트로도 하나 만들어둔다.

data = list()
for i in range(n): # n이 최대 100이고 문자열 길이가 최대 100이니 해봤자 만이다. 시간초과를 깊게 생각 안해도 된다.
    name = input()
    flag = 0
    for j in range(len(pattern)): # 패턴이 기준이기에 패턴 길이를 기준으로 넣고 반복하는게 맞다.
        if pattern[j] != '*':
            if j > len(name)-1: # 패턴이 기준이기에 name이 짧은 기준을 고려해주어야 한다. 여기서는 name이 더 짧은 경우만 고려해줬어 긴경우는 어차피 
                flag = 1        # 패턴에 더 많은 문자가 있다는 뜻이 되니까 고려할 필요가 없다.
                break
            if pattern[j] == name[j]: 
                continue
            else:
                flag = 1
                break
        else:
            break
    if flag == 1:
        print("NE")
        continue
    for j in range(len(pattern)-1,-1,-1):
        if pattern[j] != '*':
            if j > len(name)-1: # 패턴이 기준이기에 name이 짧은 기준을 고려해주어야 한다. 위 사유랑 똑같다.
                flag = 1
                break
            if pattern[j] == name[j]: 
                continue
            else:
                flag = 1
                break
        else:
            break
    if flag == 1:
        print("NE")
    else:
        print("DA")   