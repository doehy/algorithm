from itertools import combinations

N = input() #입력 받기

def thcheck(num,cnt):
    global min_result
    global max_result
    temp = 0
    if len(num) == 1: #숫자의 길이가 1일 때만 리턴
        if int(num) % 2 == 1:
            temp += 1
        min_result = min(min_result, cnt + temp)
        max_result = max(max_result, cnt + temp)
        return 
    elif len(num) == 2:
        for i in range(2):
            if int(num[i]) % 2 == 1:
                temp += 1
        thcheck(str(int(num[0]) + int(num[1])),cnt+temp)
    else:
        for i in range(3):
            if int(num[i]) % 2 == 1:
                temp += 1
        thcheck(str(int(num[0]) + int(num[1]) + int(num[2])),cnt+temp)

def cal(num,li): # 구간별로 나눠진 숫자를 더해주는 함수
    total = 0
    total = int(num[:li[0]+1])
    total += int(num[li[0]+1:li[1]+1])
    total += int(num[li[1]+1:])
    return str(total)

def focheck(num,cnt):
    temp = 0 # 현재 num에서 홀수의 개수를 기억할 변수
    if len(num) <= 3: # 숫자의 길이가 3이하인 경우 thcheck()로 출발
        thcheck(num,cnt)
    else:
        for i in range(len(num)): # 각 자릿수 별로 홀수 개수 구하기
            if int(num[i]) % 2 == 1:
                temp += 1
        data = [k for k in range(len(num))] # 현재 숫자의 길이를 인덱스 만큼 리스트에 저장
        for li in combinations(data,3): # combinations를 이용하여 3개의 조합을 얻어냄 
            focheck(cal(num,li),cnt+temp)# 현재 홀수의 갯수를 cnt에 더해서 다시 재귀
            
min_result = float("inf") #최솟값 초기화
max_result = 0 #최댓값 초기화
focheck(N,0) # dfs 시작

print(min_result, max_result) #출력