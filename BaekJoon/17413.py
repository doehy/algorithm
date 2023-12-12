text = input()

i = 0
stack = []
word = ''
while i < len(text):
    if text[i] == '<':
        if stack:
            for j in range(len(stack)):
                print(stack.pop(),end='')
        while text[i] != '>':
            word = word + text[i]
            i += 1
        word = word + text[i]
        i += 1
        print(word,end='')
        word = ''
    else:
        if text[i] != ' ':
            stack.append(text[i])
            i += 1
        elif text[i] == ' ': #공백이야
            for j in range(len(stack)):
                print(stack.pop(),end='')
            print(text[i],end='')
            i += 1

            
if stack:
    for j in range(len(stack)):
        print(stack.pop(),end='')

            
