def check(string):
    m_num = 0
    j_num = 0

    if 'a' in string or 'e' in string or 'i' in string or 'o' in string or 'u' in string:
        for i in string:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                m_num += 1
                j_num = 0
                if(m_num >= 3):
                    print('<'+string+'>' 'is' 'not' 'acceptable.')
                    return
            else:
                j_num += 1
                m_num = 0
        temp = string[0]
        for i in range(1,len(string)):
            
        return 
    else: #1번 조건을 만족하지 않았다면 
        print('<'+string+'>' 'is' 'not' 'acceptable.')
        return 

while True:
    text = input()
    if text == 'end':
        break
    else:
        check(text)