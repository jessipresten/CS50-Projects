// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>



void replace(char *input);

int main(int argc, char *argv[])
{
  if (argc != 2)
    {
       printf("usage: %s <word>\n", argv[0]);
       return 1;
    }

    char word[100];
    strcpy(word, argv[1]);
    replace(word);

    printf("new word: %s\n", word);
    return 0;

}

void replace(char *input)

{


    for (int i = 0; i < strlen(input); i++)
    {
        char c = tolower(input[i]);


        switch (c)
        {
            case 'a':
                input[i] = '6';
                break;

            case 'e':
                input[i] = '3';
                break;

            case 'i':
                input[i] = '1';
                break;

            case 'o':
                input[i] = '0';
                break;
        }
    }

}