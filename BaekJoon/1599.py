import sys
input = sys.stdin.readline
minSik = {"a": "A", "b": "B", "k":"C",
            "d": "D", "e":"E", "g":"F", 
            "h":"G", "i":"H", "l":"I",
            "m":"J", "n":"K",
            "o":"M", "p":"N", "r":"O",
            "s":"P", "t":"Q", "u":"R",
            "w":"S","y":"T"
            }

def changeMinsik(word):
    result = word.replace("ng", "L")
    for k,v in minSik.items():
        result = result.replace(k,v)
    return result

def soluction(array):
    result = dict()
    for text in array:
        temp = changeMinsik(text)
        result[text] = temp
    result = sorted(result.items(), key = lambda x : x[1])
    return result

array = []
N = int(input())
for _ in range(N):
    array.append(input().rstrip())
answer = soluction(array)
for i in answer:
    print(i[0])