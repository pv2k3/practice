#include <stdio.h>

void main(){
    int m, i, j;
    int arr[50][50];
    printf("Enter the size of the 2d matrix : ");
    scanf("%d", &m);
    printf("Enter elements\n");
    for(i=0; i<m; i++){
        for(j=0; j<m; j++){
            scanf("%d", &arr[i][j]);
        }
    }
    printf("\n");
    for(i=0; i<m; i++){
        for(j=0; j<m; j++){
            printf("%d\t", arr[j][i]);
        }
        printf("\n");
    }

}