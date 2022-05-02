number = input()

id = 0
result = 1
length = len(number)

while length > 0:
    if int(number[id:id+1]) != 0 and int(number[id:id+1]) != 1:
        result *= int(number[id:id+1])
        length -= 1
        id += 1
    else :
        if int(number[id:id+1]) ==1:
            result += 1
            length -= 1
            id += 1
        else:
            length -= 1
            id += 1

print(result)


