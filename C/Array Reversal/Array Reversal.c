// By Younes Moukhlij

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, i;
	int *arr;
	int tmp;

    scanf("%d", &num);
    arr = (int*) malloc(num * sizeof(int));
    for(i = 0; i < num; i++)
        scanf("%d", arr + i);
	i = 0;
	while (i < num / 2)
	{
		tmp = arr[i];
		arr[i] = arr[num - i - 1];
		arr[num - i - 1] = tmp;
		i++;
	}

    for(i = 0; i < num; i++)
        printf("%d ", *(arr + i));
    free (arr);
    return 0;
}
