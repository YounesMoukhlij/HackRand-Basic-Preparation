// By Younes Moukhlij
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>



int main() 
{
    int a, b;
    scanf("%d\n%d", &a, &b);
    
    for (int i = a; i <= b; i++)
    {
        if (i < 0x10)
        {
            if (i == 0x1)
                printf("one\n");
            else if (i == 0x2)
                printf("two\n");
            else if (i == 0x3)
                printf("three\n");
            else if (i == 0x4)
                printf("four\n");
            else if (i == 0x5)
                printf("five\n");
            else if (i == 0x6)
                printf("six\n");
            else if (i == 0x7)
                printf("seven\n");
            else if (i == 0x8)
                printf("eight\n");
            else if (i == 0x9)
                printf("nine\n");
        }
        else if (i > 9)
        {
            if (i % 2 == 0)
                printf("even\n");
            else
                printf("odd\n");
        }
    }

    return 0;
}
