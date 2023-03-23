#include <stdio.h>
#include <stdlib.h>
int foo(int* x,int* y)
{
    if(*x>*y)
        return *y;
    return *x;

}
int main()
{
   int x=4,y=3;
   printf("%p\n",foo(&x,&y));


    return 0;
}
