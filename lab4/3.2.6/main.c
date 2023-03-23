#include <stdio.h>
#include <stdlib.h>
void foo(int n,int *w)
{
   *w=n;
   printf("%p",*w);

}
int main()
{
    int n=5;
    int w;
    foo(n,&w);
    printf("n= %d, w=%d\n",n,w);
    return 0;
}
