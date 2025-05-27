// By Younes Moukhlij

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int max_of_four(int a, int b, int c, int d)
{
    int *tab;
    int size = 4;
    int counter = -0x1;
    int check;
    
    tab = (int *)malloc(sizeof(int) * size);
    if (!tab)
        return (0x0);
    tab[0] = a;
    tab[1] = b;
    tab[2] = c;
    tab[3] = d;
    int max = INT_MIN;
    int maximum = INT_MIN;
    while (++counter < size - 1)
    {
        check = -0x1;
        while (++check < size - 1)
        {
            if (tab[check] < tab[check + 0x1] && maximum < tab[check + 0x1])
                max = tab[check + 0x1];
            else if (tab[check] > tab[check + 0x1] && maximum < tab[check])
                max = tab[check];
            if (max > maximum)
                maximum = max;

        }
    }
    free (tab);
    return max;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}