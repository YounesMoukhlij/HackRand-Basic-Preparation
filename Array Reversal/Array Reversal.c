// By Younes Moukhlij

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, *arr, i;
	int *tab;
	int index = 0;
	int tmp;
	int size;


    scanf("%d", &num);
	size = num;
    arr = (int*) malloc(num * sizeof(int));
    for(i = 0; i < num; i++)
        scanf("%d", arr + i);

    tab = (int*) malloc(num * sizeof(int));
	if (!tab)
		return EXIT_FAILURE;
	while (index < size / 2)
	{
		tmp = tab[i];
		tab[i] = tab[num - 1];
		tab[num - 1] = tmp;
		index--;
	}
    

    /* Write the logic to reverse the array. */

    for(i = 0; i < num; i++)
        printf("%d ", *(arr + i));
    free (arr);
    return 0;
}
