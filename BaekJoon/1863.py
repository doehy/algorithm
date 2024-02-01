import sys
from collections import deque
input = sys.stdin.readline
 
def main():
    n = int(input())
    ans = 0
    st = []
    for i in range(n):
        x,y = map(int,input().split())
        if not st:
            st.append(y)
            continue
        while st and y < st[-1]:
            ans += 1
            st.pop()
        if not st or st and y > st[-1]:
            st.append(y)
    while st:
        if st[-1] > 0:
            ans += 1
        st.pop()
    print(ans)

if __name__ == '__main__':
    main()