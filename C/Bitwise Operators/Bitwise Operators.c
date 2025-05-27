#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k)
{
    int a,b;

    a = 0x1;
    b = 0x2;

    int i = 0x1;

    int temp_n = n;

    int temp_b = b;
    int counter = 1;

    int _and = 0;
    int _or = 0;
    int _xor = 0;
    int f_and = 0;
    int f_or = 0;
    int f_xor = 0;

    int tmp_and = 0;
    int tmp_or = 0;
    int tmp_xor = 0;



        while (i < temp_n)
        {
            while (b <= n)
            {

                tmp_and = a & b;
                tmp_or = a | b;
                tmp_xor = a ^ b;

                if (tmp_and > _and && tmp_and < k)
                    _and = tmp_and;
                if (tmp_or > _or && tmp_or < k)
                    _or = tmp_or;
                if (tmp_xor > _xor && tmp_xor < k)
                    _xor = tmp_xor;
                b++;
            }
            if (b == n  + 1)
            {
              temp_b++;
              b = temp_b;
            }
            if (i + 1 == temp_n)
            {
                i = 1;
                temp_n--;
            }
            a++;
            i++;
            counter++;
            tmp_or = 0;
            tmp_and = 0;
            tmp_xor = 0;

            if (_and > f_and)
                f_and = _and;
            if (_or > f_or)
                f_or = _or;
            if (_xor > f_xor)
                f_xor = _xor;
            _or = 0;
            _and = 0;
            _xor = 0;


            if (counter == n)
              break;
        }

        printf("%d\n", f_and);
        printf("%d\n", f_or);
        printf("%d\n", f_xor);
}
int main() {
    int n, k;

 scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);

    return 0;
}
