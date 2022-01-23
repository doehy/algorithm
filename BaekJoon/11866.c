#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 1001

typedef struct QueueType {
    int elem[SIZE];
    int front, rear;
}QueueType;

void init(QueueType* Q) {
    Q->front = Q->rear = 0;
}

int isEmpty(QueueType* Q)
{
    return Q->front == Q->rear;
}

int isFull(QueueType* Q)
{
    return (Q->rear + 1) % SIZE == Q->front;
}
void enqueue(QueueType* Q, int n)
{
    if (isFull(Q)) {
        printf("overflow\n");
        return;
    }
    Q->rear = (Q->rear + 1) % SIZE;
    Q->elem[Q->rear] = n;
}

int main()
{
    QueueType Q;
    init(&Q);
    int n, k;
    scanf("%d %d", &n, &k);

    for (int i = 1; i <= n; i++)
        enqueue(&Q, i);

    int num = n;
    int j;
    Q.elem[Q.front] = 0;
    n = n + 1;
    printf("<");
    while (num > 0)
    {
        for (int i = 1; i <= k; i++) {
            Q.front = (Q.front + 1) % n;
            if (Q.elem[Q.front] == 0)
                i--;
        }

        j = Q.elem[Q.front];
        if (num != 1)
            printf("%d, ", j);
        else
            printf("%d", j);
        Q.elem[Q.front] = 0;
        num--;

    }
    printf(">");
    return 0;
}