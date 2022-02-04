Number = int(input())

for i in range(Number):
    N,M = map(int,input().split())
    printList = list(map(int,input().split()))
    num = 0 #몇 번째로 출력되는지 알려줌
    checkList = [0 for _ in range(N)] 
    checkList[M] = 1 # 궁금한 문서위치 저장

    count=0
    while True:
        if printList[0] == max(printList):
            num+=1

            if checkList[0] != 1:
                del printList[0]
                del checkList[0]
            else:
                print(num)
                break
        else:
            printList.append(printList[0])
            checkList.append(checkList[0])
            del printList[0]
            del checkList[0]
