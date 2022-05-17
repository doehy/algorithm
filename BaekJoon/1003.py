from distutils.command.build_scripts import first_line_re


def fibo(n):
    if n < 2:
        return n #일단 0번째 수열과 1번쨰 수열은 0과 1로 고정되어있으니 일단 이렇게 써준다.
    else:
        fibo(n) = fibo(n-1) + fibo(n-2)





n = int(input())
print(fibo(n))
