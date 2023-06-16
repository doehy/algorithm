import sys

n = int(input())

data = []

result = 0

for i in range(n):
    data.append(sys.stdin.readline().split())

report = []
score = 0
i = 0
temp = 0
while i < n:
    if data[i][0] == '1':
        report.append(data[i])
        num = int(report[temp][2])
        num -= 1
        report[temp][2] = num
        if num == 0:
            score += int(report[temp][1])
            report.remove(report[temp])
            temp -= 1
        temp += 1
    else:
        if len(report) > 0:
            num = report[temp-1][2]
            num -= 1
            report[temp-1][2] = num
            if num == 0:
                score += int(report[temp-1][1])
                report.remove(report[temp-1])
                temp -= 1
    i += 1    

print(score)

