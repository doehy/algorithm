n = int(input())
result = (n-1) // 9 + 1
if result % 2 == 0 and n % 2 == 1:
    result += 1
print(result)



