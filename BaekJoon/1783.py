n, m = map(int, input().split())
if n == 1:
    print(1)
elif n == 2: #오른쪽으로 두 번 가는 것밖에 못하기 때문에 2로 나눠주는거임 1을 빼주는 이유는 시작점이 1이기 때문이다. 그리고 최소 한번이기때문에 1을 더함
    print(min(4, (m-1)//2+1))
elif m <= 6: #가로의길이가 6보다 작을 경우 가로의 길이만큼은 갈 수 있지만 min함수를 써서 4랑 비교를 한다. 
    print(min(4, m))
else:
    print(m-2)