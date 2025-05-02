#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(char word[]);

int main(void)
{
    // Get input words from both players
    char word1[100], word2[100];

    printf("Enter the word for player 1:  ");
    scanf("%s", word1);

    printf("Enter the word for player 2:  ");
    scanf("%s", word2);

    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    printf("Player 1 score: %d\n", score1);
    printf("Player 2 score: %d\n", score2);

    if (score1 > score2)
        printf("Player 1 wins!\n");
    else if (score1 < score2)
        printf("Player 2 wins!\n");
    else
        printf("The scores are equal\n");

    return 0;
}
// Score both words

int compute_score(char word[])

// TODO: Print the winner
{
    int score = 0;
    for (int i = 0; i < strlen(word); i++)
    {

        if (isupper(word[i]))
            score += POINTS[word[i] - 'A'];
        else if (islower(word[i]))
            score += POINTS[word[i] - 'a'];
    }
    return score;
}