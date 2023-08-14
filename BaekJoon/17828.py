import sys
input = sys.stdin.readline
n,x = map(int,input().split())
if n * 26  < x or n * 1 > x:
    print("!")
else:
    result = []
    count = x
    for i in range(1, n):
        if count - (n-i) > 25:
            result.append("Z")
            count -= 26
        else:
            tp = count - (n-i) 
            count -= tp
            result.append(chr(91 - (26 - (tp-1))))
    result.append(chr(91 - (26 - (count-1))))
    result.reverse()
    print(''.join(result))