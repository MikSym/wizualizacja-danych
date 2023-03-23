#include <stdio.h>
#include <stdlib.h>
int* foo9()
{
    return malloc(sizeof(int));
}
int main()
{
    int *wsk1=foo9();
    printf("%p\n",&wsk1);
    free(wsk1);
    return 0;
}
