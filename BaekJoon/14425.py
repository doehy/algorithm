import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s = set([input().rstrip() for _ in range(N)])
cnt = 0
for _ in range(M):
    t = input().rstrip()
    if t in s:
        cnt += 1
print(cnt)

# n, m은 최대 만개이고 입력으로 주어지는 문자열의 최대 길이는 500
# 50000000000 브루트포스를 때리면 최대 오백억인데 말이 안된다. 흠....
# 혹시 n을 500*10000을 한 후에 거기서 10000번을 해서 찾으라는 건가....
# 이거인 것 같은데