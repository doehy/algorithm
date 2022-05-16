n = input()
n_len = len(n)
result = 0
c = 0
for i in range(0,n_len-1):
    c =  9 * (10**i) * (i+1)
    result += c
result += (int(n)-(10**(n_len-1))+1)*n_len

print(result)