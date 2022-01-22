#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int queue[500000];

int main()
{
    int N;
    int front = 0;
    scanf("%d", &N);
    int back = N - 1;
    for (int i = 0; i < N; i++) {
        queue[i] = i + 1;
    }

    while (1)
    {
        front = (front + 1) % N;
        if (front == back)
            break;
        back = (back + 1) % N;
        queue[back] = queue[front];
        front = (front + 1) % N;
    }
    printf("%d", queue[back]);
    return 0;
}