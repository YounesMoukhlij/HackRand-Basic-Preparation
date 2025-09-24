#include <unistd.h>

int main(int ac, char **av)
{



    if (ac == 2)
    {
        char *s = av[1];
        int i = 0;
        while (s[i])
        {
            int j = i, count = 0;
            while (s[j] && s[j] == s[i])
            {
                count++;
                j++;
            }
            if (count > 9)
            {
                write(1, "\n", 1);
                return 0;
            }
            if (count > 1)
            {
                char c = count + '0';
                write(1, &c, 1);
            }
            write(1, &s[i], 1);
            i = j;
        }

    }
    write(1, "\n", 1);
}
