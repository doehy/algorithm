import sys
input = sys.stdin.readline
t = int(input())
result = 0
for _ in range(t):
	text = input().rstrip().split()
	print(text)
	if text[1] == "+":
		result += text[0] + text[2]
	if text[1] == "-":
		result += text[0] - text[2]
	if text[1] == "*":
		result += text[0] * text[2]
	if text[1] == "/":
		result += text[0] // text[2]
print(result)