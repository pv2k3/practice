#include <stdio.h>

void main(){
    int m, i, j, k=0;
    int arr[50][50];
    printf("Enter the size of the 2d matrix : ");
    scanf("%d", &m);
    printf("Enter elements\n");
    for(i=0; i<m; i++){
        for(j=0; j<m; j++){
            scanf("%d", &arr[i][j]);
        }
    }

    printf("Upper triangular matrix\n");
    for(i=0; i<m; i++){
        for(j=0; j < i; j++){
            printf("  ");
        }
        for(j=0; j<m-i; j++){
            printf("%d ", arr[i][k++]);
        }
        k=i+1;
        printf("\n");
    }
    k=0;
    printf("Lower triangular matrix\n");
    for(i=0; i<m; i++){
        for(j=0; j<=i; j++){
            printf("%d ", arr[i][k++]);
        }
        k=0;
        printf("\n");
    }


}