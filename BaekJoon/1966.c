#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 100

typedef struct QueueType {
    int elem[SIZE];
    int front, rear;
}QueueType;

void init(QueueType* Q)
{
    Q->front = 0;
    Q->rear = -1;
}

int isEmpty(QueueType* Q)
{
    return Q->front == Q->rear;
}

int isFull(QueueType* Q)
{
    return Q->rear == SIZE - 1;
}

void enqueue(QueueType* Q, int n)
{
    if (isFull(Q))
        printf("overflow");
    else {
        Q->rear++;
        Q->elem[Q->rear] = n;
    }
}

int dequeue(QueueType* Q)
{
    if (isEmpty(Q))
        printf("underflow");
    else {
        int temp = Q->elem[Q->front];
        Q->front++;
        return temp;
    }
}

int main()
{
    QueueType Q;
    init(&Q);

    int n;//테스트 케이스 수
    scanf("%d", &n);
    int num, m;//문서의 개수와 궁금한 index번호
    int import;//중요도
    int number = 0;//출력될 숫자
    int temp;//변하는 index를 계속 저장해줄 값
    int max;//최댓값
    int qwer; //디큐값 저장할 변수
    for (int i = 1; i <= n; i++)//테스트 케이스 수만큼 반복
    {
        scanf("%d %d", &num, &m);
        for (int j = 0; j < num; j++)//문서의 개수 만큼 입력받고 큐에 집어넣는다.
        {
            scanf("%d", &import);
            enqueue(&Q, import);
        }
        max = Q.elem[Q.front]; //0번 index가 일단 제일 크다고 가정한다.
        for (int k = 1; k < num; k++)//최대값을 찾는다.
        {
            if (Q.elem[k] > max)//최대값보다 크다면 갱신해준다
                max = Q.elem[k];
        }
        //일단 지금 이것은 무한루프를 도는데 조건이 맞다면 나가는 조건이고 front는 0으로 초기화 해놓았고 디큐는 일단 먼저 출력하고 front를 증가하는 구조로 설정해놓았다.
        while (1)
        {
            if (Q.elem[Q.front] != max && Q.front == m)//최댓값이 아닌데 찾는 인덱스야
            {
                qwer = dequeue(&Q);
                enqueue(&Q, qwer);
                m = Q.rear;
            }
            else if (Q.elem[Q.front] != max && Q.front == m)//최댓값이 아닌데 찾는 인덱스도 아님
            {
                qwer = dequeue(&Q);
                enqueue(&Q, qwer);
            }
            else if (Q.elem[Q.front] == max && Q.front != m) //최댓값인데 찾는 인덱스가 아니야
            {
                dequeue(&Q);
                max = Q.elem[Q.front];
                for (int q= Q.elem[Q.front]; q <= Q.elem[Q.rear]; q++)//최대값을 찾는다.
                {
                    if (Q.elem[q] > max)//최대값보다 크다면 갱신해준다
                        max = Q.elem[q];
                }
            }

            else if (Q.elem[Q.front] == max && Q.front == m)//최댓값인데 찾는 인덱스야
            {
                number++;
                printf("%d", Q.elem[Q.front]);
                break;
            }
        }
    }
    return 0;
}
