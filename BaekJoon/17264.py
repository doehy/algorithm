N,P = map(int,input().split())
w,l,g = map(int,input().split())

score =0

people = {}
answer = "I AM IRONMAN!!"

for _ in range(P):
    tmp_name,WinOrLose = input().split()
    people[tmp_name] = WinOrLose

for _ in range(N):
    name = input()
    if name in people and people[name] == "W":
        score += w
    else:
        score -= l
        if score < 0:
            score = 0
    if score >= g:
        answer = "I AM NOT IRONMAN!!"

print(answer)