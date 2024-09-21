// By YOunes MOukhlij

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


int marks_summation(int* marks, int number_of_students, char gender)
{
    int sum = 0x0;
    
    (void) gender;
    if (number_of_students > 0x2)
    {
        for (int i = 0x0; i < number_of_students ; i += 0x1)
        {
            if (gender == 'b')
            {
                if (i % 0x2 == 0x0)
                    sum += marks[i];
            }
            else if (gender == 'g')
            {
                if (i % 0x2 != 0x0)
                    sum += marks[i];
            }
        }
    }
    else
        sum = 0x0;
    return (sum);
}

int main() {
    int number_of_students;
    char gender;
    int sum;
  
    scanf("%d", &number_of_students);
    int *marks = (int *) malloc(number_of_students * sizeof (int));
 
    for (int student = 0; student < number_of_students; student++) {
        scanf("%d", (marks + student));
    }
    
    scanf(" %c", &gender);
    sum = marks_summation(marks, number_of_students, gender);
    printf("%d", sum);
    free(marks);
 
    return 0;
}
