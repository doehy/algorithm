#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 2000000

typedef int element;

typedef struct QueueType {
	element elem[SIZE];
	int front, back;
}QueueType;

void init (QueueType *Q){
	Q->front = Q->back = -1;
    return ;
}

void push(QueueType* Q,int n) {
	Q->back++;
	Q->elem[Q->back] = n;
    return ;
}

void pop(QueueType* Q) {
	if (Q->front == Q->back){
		printf("%d\n", -1);
        return ;
    }
	else {
		Q->front++;
		printf("%d\n", Q->elem[Q->front]);
        return ;
	}
}

void size(QueueType* Q)
{
	printf("%d\n", Q->back - Q->front);
    return ;
}

void empty(QueueType* Q)
{
	if (Q->front == Q->back){
		printf("%d\n", 1);
        return ;
    }
	else{
		printf("%d\n", 0);
        return ;
    }
}

void front(QueueType* Q)
{
	if (Q->front == Q->back){
		printf("%d\n", -1);
        return ;
    }
	else{
		printf("%d\n", Q->elem[Q->front + 1]);
        return ;
    }
}

void back(QueueType* Q)
{
	if (Q->front == Q->back){
		printf("%d\n", -1);
        return ;
    }
	else{
		printf("%d\n", Q->elem[Q->back]);
        return ;
    }
}

int main()
{
	QueueType Q;
	init(&Q);
	int num;
	scanf("%d", &num);
	char text[10];
	int n = 0;
	for (int i = 0; i < num; i++)
	{
		scanf("%s", text);
		if (strcmp(text, "push") == 0)
		{
			scanf("%d", &n);
			push(&Q, n);
		}
		else if (strcmp(text, "pop") == 0)
			pop(&Q);
		else if (strcmp(text, "size") == 0)
			size(&Q);
		else if (strcmp(text, "empty") == 0)
			empty(&Q);
		else if (strcmp(text, "front") == 0)
			front(&Q);
		else if (strcmp(text, "back") == 0)
			back(&Q);
	}
	return 0;
}