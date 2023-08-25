import sys
input = sys.stdin.readline
t = int(input())

def isSimilar(text, left, right):
    while left < right:
        if text[left] == text[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def isPalindrome(text, left, right):
    if text == text[::-1]:
        return 0
    else:
        while left < right:
            if text[left] != text[right]:
                check_left = isSimilar(text, left + 1, right)
                check_right = isSimilar(text, left, right - 1)

                if check_left or check_right:
                    return 1
                else:
                    return 2
            else:
                left += 1
                right -= 1

for _ in range(t):
    text = input().rstrip()
    left, right = 0, len(text)-1
    answer = isPalindrome(text, left, right)
    print(answer)