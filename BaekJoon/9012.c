#include <stdio.h>
#include<stdlib.h>
#include <string.h>

char stack[1000];
int count = 0;

void push(int n)
{
    stack[count] = n;
    count++;
}

void pop()
{
    count--;
    stack[count] = 0;
}


int main()
{
    int n;
    scanf("%d", &n);
    char text[50];
    for (int i = 0; i < n; i++) {
        scanf("%s", text);
        int len = strlen(text);
        int cnt = 0;
        for (int j = 0; j < len; j++)
        {
            if (cnt < 0)
                break;
            if (text[j] == '(') {
                cnt++;
            }
            else if (text[j] == ')')
                cnt--;
        }
        if (cnt == 0)
            printf("YES\n");
        else if(cnt != 0)
             printf("NO\n");
    }
}