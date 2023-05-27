import sys

n = int(input())
data = set()
for i in range(n):
    name,ox = sys.stdin.readline().split()
    if ox == 'enter':
        data.add(name)
    else:
        if name in data:
            data.remove(name)
    
data=sorted(data,reverse=True)
print('\n'.join(data))