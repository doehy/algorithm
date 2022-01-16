#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 100

typedef char element;
typedef struct QueueType {
	element elem[SIZE];
	int front, rear;
}QueueType;

void initQueue(QueueType* Q)
{
	Q->front = Q->rear = -1; // front와 rear를 스택과 동일하게 -1로 초기화
}

int isEmpty(QueueType* Q)
{
	return Q->front == Q->rear; //front와 rear가 같으면 큐는 비워져있다.
}

int isFull(QueueType* Q) //배열의 경우에는 사이즈가 한정되어있으니 풀을 정의해주는거다.
{
	return Q->rear == SIZE - 1;
}

void enqueue(QueueType* Q, char e)
{
	if (isFull(Q))
	{
		printf("Full\n");
		return;
	}
	Q->rear++;
	Q->elem[Q->rear] = e;
}

element dequeue(QueueType* Q)
{
	if (isEmpty(Q))
	{
		printf("비워있따.");
		return;
	}
	Q->front++; 
	return Q->elem[Q->front]; //안에있는 값이 삭제 됐다고 생각하지만 실제로는 남아있다.
}

element peek(QueueType* Q)
{
	if (isEmpty(Q))
	{
		printf("비워있따.");
		return;
	}
	return Q->elem[Q->front+1]; 
}

void print(QueueType* Q)
{
	printf("front pos : %d , rear pos : %d\n", Q->front, Q->rear);

	if (!isEmpty(Q))
	{
		for (int i = Q->front + 1; i <= Q->rear; i++)//front는 값이 있는 바론 전 값을 가리키니 +1해주는거임
			printf("[%c]", Q->elem[i]);
		printf("\n");

	}
}


int main()
{
	QueueType Q;
	initQueue(&Q);
	srand(time(NULL));

	for (int i = 0; i < 7; i++) //일단 7까지
	{
		enqueue(&Q, rand() % 26 + 65); //이러면 아스키코드값 대문자가 나옵니다.
	}
	print(&Q);

	for (int i = 0; i < 3; i++) //일단 3까지
		printf("[%c]", dequeue(&Q));
	printf("\n\n");
	print(&Q);
	printf("\n");
	printf("[%c]",peek(&Q));
	printf("\n");
	print(&Q);

	for (int i = 0; i < 5; i++) 
	{
		enqueue(&Q, rand() % 26 + 65); //이러면 아스키코드값 대문자가 나옵니다.
	}
	print(&Q);

	for (int i = 0; i < 3; i++) 
		printf("[%c]", dequeue(&Q));
	printf("\n\n");
	print(&Q);
	printf("\n");
	return 0;
}