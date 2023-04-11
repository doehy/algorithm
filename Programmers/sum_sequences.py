from collections import defaultdict

def solution(sequence, k):
    s = defaultdict(list)
    temp = 0
    left, right = 0, 0
    temp, i = 0, 0
    while right < len(sequence) and left < len(sequence): 
        if i == 0:
            temp = sequence[0]
            if temp == k:
                s[right+1-left].append([left,right])
            right += 1 # 처음에는 일단 right가 넘어가는게 맞음
            if not right < len(sequence):
                break
            temp += sequence[right]
            i += 1
        else:
            if temp == k:
                s[right+1-left].append([left,right])
                temp -= sequence[left]
                left += 1
                right += 1
                if not right < len(sequence):
                    break
                temp += sequence[right]
            elif temp > k:
                temp -= sequence[left]
                left += 1
            else:
                right += 1
                if not right < len(sequence):
                    break
                temp += sequence[right]
    
    min_len = min(s.keys())
    min_list = s[min_len]
    min_list = sorted(min_list, key=lambda x:x[0])
    answer = min_list[0]
    return answer