#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

char randomChoice()
{
    srand(time(NULL));
    int cho_num = rand() % 3;
    if (cho_num == 0)
    {
        return 'r';
    }
    else if (cho_num == 1)
    {
        return 'p';
    }
    else if (cho_num == 2)
    {
        return 's';
    }
    else
    {
        return 'X';
    }
}

int main(void)
{
    char comp_cho = randomChoice();
    char user_cho;

    printf("computer thinking.\n");
    sleep(1);
    if (comp_cho != 'r' && comp_cho != 'p' && comp_cho != 's')
    {
        printf("Something went wrong...");
        exit(EXIT_FAILURE);
    }

    printf("The computer has played\n\nEnter your guess('r' or 'p' or 's') :");
    scanf("%c", &user_cho);

    if (user_cho == comp_cho)
    {
        printf("\nIts a tie");
    }
    else if (user_cho == 'r')
    {
        if (comp_cho == 's')
        {
            printf("\nYou won");
        }
        else if (comp_cho == 'p')
        {
            printf("\nYou Lose");
        }
    }
    else if (user_cho == 'p')
    {
        if (comp_cho == 'r')
        {
            printf("\nYou won");
        }
        else if (comp_cho == 's')
        {
            printf("\nYou Lose");
        }
    }
    else if (user_cho == 's')
    {
        if (comp_cho == 'p')
        {
            printf("\nYou won");
        }
        else if (comp_cho == 'r')
        {
            printf("\nYou Lose");
        }
    }
    else
    {
        printf("\n\nplease choose from 'r' or 'p' or 's'");
    }

    printf("\n\nThe computer played %c\n", comp_cho);

    return 0;
}