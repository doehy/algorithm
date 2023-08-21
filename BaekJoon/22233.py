# 메모장에 적혀 있는 키워드의 개수가 최대 이십만개, 블로그에 쓴 글의 개수가 최대 이십만개
# 한 글당 최대 키워드는 10개, 키워드 길이는 최대 열 글자
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
data = set()
for _ in range(n):
    text = input().rstrip()
    data.add(text)

for _ in range(m):
    text = input().rstrip().split(",")
    for tp in text:
        if tp in data:
            data.remove(tp)
    print(len(data))
