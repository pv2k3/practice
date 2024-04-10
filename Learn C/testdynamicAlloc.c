#include <stdio.h>
#include <alloca.h>

void main(){
    int i, n;
    int *ptr;
    printf("ENter the number of elements : ");
    scanf("%d", &n);
    ptr = (int*)malloc(n*sizeof(int));

    for (i=0; i < n; i++){
        ptr[i]=i;
    }

    for (i = 0; i < n; i++){
        printf(" %d", ptr[i]);
    }
    
    free(ptr);
    free(&n);
    printf("\n");

    printf("%d", n);
}