#include <stdio.h>
#include <string.h>

#define SIZE 100

int stack[10001];
int count = 0;

void push(int n)
{
    stack[count] = n;
    count++;
}

void pop()
{
    if (count != 0)
    {
        count--;
        printf("%d\n", stack[count]);
        stack[count] = 0;
    }
    else
        printf("%d\n",-1);
}

void size()
{
    printf("%d\n", count);
}

void empty()
{
    if (count == 0)
        printf("%d\n",1);
    else
        printf("%d\n",0);
}
void top()
{
    if (count != 0)
        printf("%d\n", stack[count-1]);
    else
        printf("%d\n",-1);
}

int main()
{
    int n, number; 
    scanf("%d", &n);
    char m[10];
  
    for(int i =0; i< n; i++)
    {
        scanf("%s", m);
        if (strcmp(m, "push") == 0) {
            scanf("%d", &number);
            push(number);
        }
        else if (strcmp(m, "pop") == 0)
               pop();
        else if (strcmp(m, "top") == 0)
               top();
        else if (strcmp(m, "empty") == 0)
                empty();
        else if (strcmp(m, "size") == 0)
                size();
    }
    return 0;
}