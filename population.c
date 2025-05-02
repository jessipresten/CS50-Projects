#include <cs50.h>
#include <stdio.h>

int main(void)
{

    // TODO: Prompt for start size

      int x;
       do
     {

    x = get_int( "start size: ");
     }
        while (x < 10);


    // TODO: Prompt for end size
      int y;
       do
      {
       y = get_int ("end size: ");
      }

       while(y < x);


    // TODO: Calculate number of years until we reach threshold

        int z=0;
        while (x< y)
    {

     x = x + (x / 3) - (x / 4);
     z++;
    }

    // TODO: Print number of years

printf( "Years: %i\n", z);
return 0;
}