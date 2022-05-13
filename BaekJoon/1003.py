def fibo(n):
    memo[0]=0
    memo[1]=1

    if n<2:
        return memo(n)
    for i in range(2,n+1):
        memo[i] = memo[i-2] + memo[i-1]

    return memo[n]

n = int(input())
memo = [0 for i in range(n+1)]
print(fibo(n))
