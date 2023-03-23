#include <stdio.h>
#include <stdlib.h>
int foo(int const *a,int const *b)
{
  return *a+*b;
}
int main()
{
   int const a=8,b=3;
   printf("%d",foo(&a,&b));
   return 0;
}
