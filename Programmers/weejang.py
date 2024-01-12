from itertools import combinations

def solution(clothes):
    answer = 0
    data = dict()
    for name,kind in clothes:
        if kind not in data:
            data[kind] = 1
        else:
            data[kind] += 1
    
    answer += sum(data.values())
    temp = 1
    for i in data.values():
        temp * i
    answer += temp
    return answer

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))