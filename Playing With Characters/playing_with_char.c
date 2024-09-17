// By Younes Moukhlij

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    char ch;
    char s[100];
    char sen[100];
    
    scanf("%c", &ch);  // Read a single character

    scanf("%s", s);  // Read a full sentence (including spaces)
    scanf(" %[^\n]%*c", sen);  // Read a full sentence (including spaces)
    printf("%c\n", ch);  // Print the character
    printf("%s\n", s);   // Print the string
    printf("%s\n", sen); // Print the sentence
    
    return 0;
}

