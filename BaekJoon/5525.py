n = int(input())
m = int(input())
text = input() # 일단 String으로 입력 받고
idx = 0 # 전체적인 idx 흐름을 기억해둘 변수
result = 0
count = 0
while idx < m-2: # text길이보다 작은 동안
    if text[idx:idx+3] == 'IOI':
        count += 1
        idx += 2
        if count == n:
            result += 1
            count -= 1
    else:
        idx += 1
        count = 0

print(result)
# n이 최대 백만, text의 최소 3부터 최대 백만 
# 시간제한이 1초인데 이게 통과가 돼? 안 됐어
# 흠 시간 초과를 어떻게 없애 
