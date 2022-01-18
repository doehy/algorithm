#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 10
typedef char element;
typedef struct QueueType {
	element elem[SIZE];
	int front, rear;
}DequeType;

void initDeque(DequeType* D)
{
	D->front = D->rear = 0; // front와 rear를 선형큐와 달리 0으로 초기화
}

int isEmpty(DequeType* D)
{
	return D->front == D->rear; //front와 rear가 같으면 큐는 비워져있다.
}

int isFull(DequeType* D) //배열의 경우에는 사이즈가 한정되어있으니 풀을 정의해주는거다.
{
	return (D->rear+1) % SIZE == D->front; //원형큐와 똑같다.
}

void addFront(DequeType* D, char e)
{
	if (isFull(D))
	{
		printf("Full\n");
	}
	D->elem[D->front] = e;
	D->front = (D->front - 1 + SIZE) % SIZE;
}

void addRear(DequeType* D, char e) //원형큐에 enqueue와 똑같은 것이다.
{
	if (isFull(D))
	{
		printf("Full\n");
	}
	D->rear = (D->rear+1) % SIZE ; 
	D->elem[D->rear] = e;
}

element deleteFront(DequeType* D) //원형큐에 dequeue와 같은것임.
{
	if (isEmpty(D))
	{
		printf("비워있따.");
		return 0;
	}
	D->front = (D->front +1) %SIZE;
	return D->elem[D->front]; //안에있는 값이 삭제 됐다고 생각하지만 실제로는 남아있다.
}

element deleteRear(DequeType* D)
{
	if (isEmpty(D))
	{
		printf("Empty\n");
		return 0;
	}
	int pos = D->rear;
	D->rear = (D->rear - 1 + SIZE) % SIZE;
	return D->elem[pos];
}

element getFront(DequeType* D) //원형큐에 peek와 같은 것이다.
{
	if (isEmpty(D))
	{
		printf("비워있따.");
		return 0;
	}
	return D->elem[(D->front + 1) % SIZE];
}

element getRear(DequeType* D)
{
	if (isEmpty(D))
	{
		printf("Empty\n");
		return 0;
	}
	return D->elem[D->rear];
}
void print(DequeType* D)
{
	printf("front pos : %d , rear pos : %d\n", D->front, D->rear);

	if (!isEmpty(D))
	{
		int i = D->front; 
		do
		{
			i = (i + 1) % SIZE;
			printf("[%c]", D->elem[i]);
			if (i == D->rear) // rear를 만났다는거면 다 출력했다는 소리니 break를 하는거임
				break;
		} while (i != D->front); //front를 만나지 못한다 그래서 rear를 만날 때 까지 반복하겠다는 소리이다.
	}
	printf("\n");
}


int main()
{
	DequeType D;
	initDeque(&D);
	srand(time(NULL));

	for (int i = 0; i < 7; i++) //일단 7까지 해준거임.
	{
		addRear(&D, rand() % 26 + 65); //이러면 아스키코드값 대문자가 나온다
	}
	print(&D);
	
	for (int i = 0; i < 3; i++) //일단 3까지 해준거임.
		printf("[%c]", deleteFront(&D));
	printf("\n\n");
	print(&D);

	printf("\n");

	for (int i = 0; i < 5; i++)
	{
		addFront(&D ,rand() % 26 + 65); //이러면 아스키코드값 대문자가 나온다
	}
	print(&D);

	for (int i = 0; i < 3; i++) 
		printf("[%c]", deleteRear(&D));
	printf("\n\n");
	print(&D);
	printf("\n");
	return 0;
}