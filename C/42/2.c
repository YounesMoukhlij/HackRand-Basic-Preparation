#include <unistd.h>

void nth_char(char *s, int n)
{
    int i = n - 1;
    if (!s[0] || n < 1)
    {
        write(1, "\n", 1);
        return ;
    }
    while (s[i])
    {
        write(1, &s[i], 1);
        i += n;
    }
    write(1, "\n", 1);
}



int main()
{
    nth_char("world", 2);
}
