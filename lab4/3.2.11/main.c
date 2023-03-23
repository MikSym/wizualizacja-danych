#include <stdio.h>
#include <stdlib.h>

int * foo11(int n)
{

    return malloc(n*sizeof(int));
}
int main()
{
    int *wsk2=foo11(6);
    printf("%p\n",&wsk2);
    free(wsk2);
    return 0;
}
