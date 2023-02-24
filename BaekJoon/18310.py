import sys
input = sys.stdin.readline

N = int(input())
house = list(map(int,input().split()))

house.sort()
print(house[(N-1) // 2])


# 안테나는 집이 있는 곳에만 설치할 수 있어
# 최대 이십만이기때문에 완전탐색하면 시간초과야

