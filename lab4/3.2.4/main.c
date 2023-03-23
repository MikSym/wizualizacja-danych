#include <stdio.h>
#include <stdlib.h>
void zamiana(int *a,int *b)
{
    if(*a>*b)
    {
      int temp=*a;
      *a=*b;
      *b=temp;


    }

}
int main()
{
   int a=4,b=3;
   printf("a=%d, b=%d\n",a,b);
   zamiana(&a,&b);
   printf("a=%d, b=%d\n",a,b);


    return 0;
}
