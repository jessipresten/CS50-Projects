#include <cs50.h>
#include <stdio.h>

int main (void)
{
  int height, row, column, space;
  do
  {
    height=get_int("height:  ");
   }
   while (height<1 || height>8);

//find rows

   for (row=0; row< height; row ++)
  {

//find space
   for (space=0; space<height-row-1; space++)
  {
    printf(" ");
  }

//find column
   for (column=0; column<= row; column++)
  {
    printf ("#");
  }
    printf("\n");
  }
return 0;
}
