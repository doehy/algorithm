from itertools import permutations

def solution(numbers):
    answer = ''
    max_number = 0
    for number in permutations(numbers,len(numbers)):
        temp = int(''.join(str(_) for _ in number))
        max_number = max(max_number,temp)
    answer = str(max_number)
    return answer

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))