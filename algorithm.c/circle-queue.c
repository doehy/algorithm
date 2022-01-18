#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 10

typedef char element;
typedef struct QueueType {
	element elem[SIZE];
	int front, rear;
}QueueType;

void initQueue(QueueType* Q)
{
	Q->front = Q->rear = 0; // front와 rear를 선형큐와 달리 0으로 초기화
}

int isEmpty(QueueType* Q)
{
	return Q->front == Q->rear; //front와 rear가 같으면 큐는 비워져있다.
}

int isFull(QueueType* Q) //배열의 경우에는 사이즈가 한정되어있으니 풀을 정의해주는거다.
{
	return (Q->rear+1) % SIZE == Q->front; //선형큐와 다르다.
}

void enqueue(QueueType* Q, char e)
{
	if (isFull(Q))
	{
		printf("Full\n");
		return;
	}
	Q->rear = (Q->rear+1) % SIZE ;  //선형큐와 다르다.
	Q->elem[Q->rear] = e;
}

element dequeue(QueueType* Q)
{
	if (isEmpty(Q))
	{
		printf("비워있따.");
		return;
	}
	Q->front = (Q->front +1) %SIZE; //선형큐와 다르다.
	return Q->elem[Q->front]; //안에있는 값이 삭제 됐다고 생각하지만 실제로는 남아있다.
}

element peek(QueueType* Q)
{
	if (isEmpty(Q))
	{
		printf("비워있따.");
		return;
	}
	return Q->elem[(Q->front+1)%SIZE]; //선형큐와 다르다. 
}

void print(QueueType* Q)
{
	printf("front pos : %d , rear pos : %d\n", Q->front, Q->rear);

	if (!isEmpty(Q))
	{
		int i = Q->front; 
		do
		{
			i = (i + 1) % SIZE;
			printf("[%c]", Q->elem[i]);
			if (i == Q->rear) // rear를 만났다는거면 다 출력했다는 소리니 break를 하는거임
				break;
		} while (i != Q->front); //어차피 front를 못 만나 그니까 그냥 rear를 만날 때 까지 반복하겠다는 소리임.
	}
	printf("\n");
}


int main()
{
	QueueType Q;
	initQueue(&Q);
	srand(time(NULL));

	for (int i = 0; i < 7; i++) //일단 7까지 해준거임.
	{
		enqueue(&Q, rand() % 26 + 65); //이러면 아스키코드값 대문자가 나온다고? 일단.
	}
	print(&Q);

	for (int i = 0; i < 3; i++) //일단 3까지 해준거임.
		printf("[%c]", dequeue(&Q));
	printf("\n\n");
	print(&Q);
	printf("\n");
	printf("[%c]",peek(&Q));
	printf("\n");
	print(&Q);

	for (int i = 0; i < 5; i++) //일단 7까지 해준거임.
	{
		enqueue(&Q, rand() % 26 + 65); //이러면 아스키코드값 대문자가 나온다고? 일단.
	}
	print(&Q);

	for (int i = 0; i < 3; i++) //일단 3까지 해준거임.
		printf("[%c]", dequeue(&Q));
	printf("\n\n");
	print(&Q);
	printf("\n");
	return 0;
}