#include <stdio.h>
#include <stdlib.h>
int* foo10()
{
    return malloc(sizeof(double));
}
int main()
{
    double *wsk1=foo10();
    printf("%p\n",&wsk1);
    free(wsk1);
    return 0;
}
