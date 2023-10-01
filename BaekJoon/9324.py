n = int(input())

def check(text):
    data = dict()
    for i in range(len(text)):
        if text[i] not in data:
            data[text[i]] = 1
        else:
            data[text[i]] += 1
        if data[text[i]] == 3:
            data[text[i]] = -1
            if i+1 < len(text):
                if text[i+1] == text[i]:
                    pass
                else:
                    print("FAKE")
                    return
            elif i == len(text) -1:
                print("FAKE")
                return
    print("OK")
    return

for i in range(n):
    text = input()
    check(text)