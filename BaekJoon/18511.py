def sol(order, num):
    global final_ans

    if order == len(str(N)): 
        final_ans = max(final_ans, num) 
        return

    for i in range(K): # K의 원소가 그 자릿수에 들어갈 수 있는지 살펴보기(큰 자릿수부터 채움)
        now_num = arr[i]*(10**(len(str(N))-order-1)) + num 

        if now_num <= N: # now_num이 N 이하인 경우
            sol(order + 1, now_num)

        else: # now_num이 N보다 크면
            sol(order+1, num)


N, K = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort(reverse=True) # 큰 수부터 넣어보려고

final_ans= 0
sol(0, 0) # 자릿수 몇번째인지, 그때까지 만든 숫자

# print(ans_list)
print(final_ans)
