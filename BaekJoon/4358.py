from collections import defaultdict
import sys
input = sys.stdin.readline

trees = defaultdict(int)
n = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    trees[tree] += 1
    n += 1

result = list(trees.keys())
result.sort()
for tree in result:
    print('%s %.4f' %(tree, trees[tree]/n*100))

# 최대 30글자 입력이 최대 백만 개 그렇다면 최대 삼천만 개

