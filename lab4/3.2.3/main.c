#include <stdio.h>
#include <stdlib.h>
void zamiana(int *a,int *b)
{
    int temp=*a;
    *a=*b;
    *b=temp;

}
int main()
{
   int a=1,b=3;
   printf("a=%d, b=%d\n",a,b);
   zamiana(&a,&b);
   printf("a=%d, b=%d\n",a,b);


    return 0;
}
