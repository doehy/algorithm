#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char text[101];
    scanf("%s",text);
    int num = 0;
    int number =0;
    int len = strlen(text);
    int temp  =0;
    for(int i=0; i < len;i++)
    {
        if(text[i] == '(' || text[i] == '{' || text[i] == '[')
        {
            if(text[i] == '(')
                num += 1;
            else if(text[i] == '{')
                num += 2;
            else if(text[i] == '[')
            num += 3;
        }
        else if(text[i] == ')' || text[i] == '}' || text[i] == ']')
        {
            if(text[i] == ')')
                num -= 1;
            else if(text[i] == '}')
                num -= 2;
            else if(text[i] == ']')
                num -= 3;
        }
        else
        {
            if(num > number)
                number = num;
        }
        
    }
    printf("%d",number);
    return 0;
}