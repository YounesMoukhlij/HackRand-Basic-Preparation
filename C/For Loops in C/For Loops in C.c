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
        if (i <= 0x9)
        {
            if (i == 0x1)
                printf("one");
            else if (i == 0x2)
                printf("two");
            else if (i == 0x3)
                printf("three");
            else if (i == 0x4)
                printf("four");
            else if (i == 0x5)
                printf("five");
            else if (i == 0x6)
                printf("six");
            else if (i == 0x7)
                printf("seven");
            else if (i == 0x8)
                printf("eight");
            else if (i == 0x9)
                printf("nine");
        	printf("\n");
        }
        if (i > 9)
        {
            if (i % 2 == 0)
                printf("even");
            else
                printf("odd");
        	printf("\n");
        }
    }

    return 0;
}
