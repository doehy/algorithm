# 입력으로 주어지는 모든 정수가 천보다 작거나 같다고 하는 것을 보면 백트래킹은 아니다 백트래킹을 할 시 무조건 리커젼에러에 걸릴 것 이다.
# 각 화학 조합품마다 만들 수 있는 최대 개수들이 있다. 각 화학 조합품에 대해서 반복문을 돈다.
t = int(input())

for i in range(t): # 테스트 케이스 개수만큼
    max_result =0
    a,b,c = map(int,input().split())
    ab,bc,ca = map(int,input().split())
    ab_c = b if a > b else a
    for i in range(ab_c+1):
        bc_c = min(b-i,c)
        ca_c = min(c-bc_c,a-i)
        max_result = max(max_result,i*ab + bc_c*bc + ca_c*ca)

        ca_c = min(a-i,c);
        bc_c = min(b-i,c-ca_c)
        max_result = max(max_result,i*ab + bc_c*bc + ca_c*ca)
    print(max_result)

        
            



    

        


        

            
    