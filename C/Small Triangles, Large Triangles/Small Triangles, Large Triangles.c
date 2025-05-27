// By Younes Moukhlij

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;
void sort_by_area(triangle* tr, int n)
{
    double area[n], s;
    int i;
    for(i = 0; i < n; i++)
	{
        s = (tr[i].a + tr[i].b + tr[i].c ) / 2.0;

        area[i] = sqrt(s * (s - tr[i].a) * (s - tr[i].b) * (s - tr[i].c));
    }

    int j, k;
    double tempArea;
    struct triangle temp;
    for(k = 0; k < n; k++){
        for(j = 0; j < n - k - 1; j++){
            if(area[j] > area[j + 1]){
                temp = tr[j];
                tr[j] = tr[j + 1];
                tr[j + 1] = temp;

                tempArea = area[j];
                area[j] = area[j + 1];
                area[j + 1] = tempArea;
            }
        }
    }
}

int main()
{
	int n = 3;
	// scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));

	tr[0].a = 7, tr[0].b = 24, tr[0].c = 5;
	tr[1].a = 12, tr[1].b = 12, tr[1].c = 13;
	tr[2].a = 3, tr[2].b = 4, tr[2].c = 5;
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}

// 3
// 7 24 25
// 5 12 13
// 3 4 5