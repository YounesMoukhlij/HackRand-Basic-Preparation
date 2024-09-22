//By Younes Moukhlij

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int *tab;
    int size;
    int sum = 0x0;
    
    scanf("%d\n", &size);
    tab = (int *)malloc(sizeof(int) * size);
    if (!tab)
        return (EXIT_FAILURE);
    for (int i = 0x0;i < size; i++)
    {
        scanf("%d", &tab[i]);   
    }
    for (int j = 0x0;j < size; j++)
    {
        sum += tab[j];
    }
    printf("%d\n", sum);
    free(tab);
    return EXIT_SUCCESS;
}