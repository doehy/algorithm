#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 100

typedef char element;

typedef struct StackType
{
	element elem[SIZE];
	int top;
}StackType;

void init(StackType* S)
{
	S->top = -1;
}

int isEmpty(StackType* S)
{
	return S->top == -1;
}

int isFull(StackType* S)
{
	return S->top == SIZE - 1;
}

void push(StackType* S, element e)
{
	if (isFull(S)) {
		printf("Over flow\n");
		return;
	}
	S->top++;
	S->elem[S->top] = e;
}

element pop(StackType* S)
{
	if (isEmpty(S)) {
		printf("underflow\n");
		return 0;
	}
	element temp = S->elem[S->top];
	S->top--;
	return temp;
}

element peek(StackType* S)
{
	return S->elem[S->top];
}

void print(StackType* S)
{
	for (int i = 0; i <= S->top; i++)
		printf("%c\t", S->elem[i]);
}

int isBalanced(char* str)
{
	StackType S;
	init(&S);
	char c, t; //괄호를 비교하기 위해 만든 문자
	int n = strlen(str);
	for (int i = 0; i < n; i++)
	{
		c = str[i];		//i번째에 값을 c에다가 넣는다.
		if (c == '(' || c == '{' || c == '[')
			push(&S, c);
		else if (c == ')' || c == '}' || c == ']')
		{
			if (isEmpty(&S))
				return 0;
			else
			{
				t = pop(&S);
				if ((c == ')' && t != '(') || (c == '}' && t != '{') || (c == ']' && t != '['))
					return 0;
			}
		}
	}
	return isEmpty(&S);
}

int prec(char op)
{
	switch (op)
	{
	case '(': case')':
		return 0;	break;
	case '+': case'-':
		return 1;	break;
	case '*': case'/':
		return 2;	break;
	}
}

void convert(char* str)		//후위 수식으로 변환하는 코드
{
	StackType S;
	init(&S);
	char c,t;
	int n = strlen(str);

	for (int i = 0; i < n; i++)
	{
		c = str[i];
		switch (c) {
			case '+':case '-':case '/':case '*':
				while (!isEmpty(&S) && (prec(c) <= prec(peek(&S))))
					printf("%c",pop(&S));	//pop해서 출력
				push(&S, c);	break;		//조건에 해당안되면 일단 들어가 ex)처음 것이거나 연산우선수위가 더 낮을경우
			case '(':
				push(&S, c);		break;	//'('는일단 스택에 들어간다
			case ')':
				t = pop(&S);		//')'는일단 t에다가 pop해서 집어넣고 t가 (가 나올 떄까지 계속 출력을 한다.
				while (t != '(')
				{
					printf("%c", t);
					t = pop(&S);
				}
				break;
			default :
				printf("%c", c); break;	//피연산자인경우 스택에 들어가지 않으니 걍 바로바로 출력해준다.
		}
		
	}
	while (!isEmpty(&S))
		printf("%c", pop(&S));
	printf("\n");
}
void main()
{
	char expr[SIZE];
	printf("input");
	scanf("%s", expr);
	convert(expr);
	
}