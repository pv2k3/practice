#include <stdio.h>
// #include <conio.h>

void multiplyMatrix(int arr1[10][10], int r1, int c1, int arr2[10][10], int r2, int c2, int multiply[10][10]);

void makeArray(int arr[10][10], int r, int c);

void printArray(int arr[10][10], int r, int c);

void main(){
    int arr1[10][10], r1, c1, arr2[10][10], r2, c2, multiply[10][10];
    // clrscr();
    printf("Enter the num of rows and column in array 1  : ");
    scanf("%d %d", &r1, &c1);
    makeArray(arr1, r1, c1);

    printf("Enter the num of rows and column in array 1  : ");
    scanf("%d %d", &r2, &c2);
    makeArray(arr2, r2, c2);
    
    multiplyMatrix(arr1, r1, c1, arr2, r2, c2, multiply);
    
    // getch();
}

void multiplyMatrix(int arr1[10][10], int r1, int c1, int arr2[10][10], int r2, int c2, int multiply[10][10]){
    if (c1 != r2) {
        printf("Wrong input array cannot be multiplied\n");
        return;
    }

    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++) {
            for (int k = 0; k < c1; k++) {
                multiply[i][j] += arr1[i][k]*arr2[k][j];
            }
        }
    }
    
    printArray(multiply, r1, c2);
}

void makeArray(int arr[10][10], int r, int c){
    int i, j;
    printf("Enter elements\n");
    for (i=0; i < r; i++){
        for(j=0; j<c; j++){
            scanf("%d", &arr[i][j]);
        }
    }
}

void printArray(int arr[10][10], int r, int c){
    int i, j;
    printf("Print elements\n");
    for (i=0; i < r; i++){
        for(j=0; j<c; j++){
            printf("%d\t", arr[i][j]);
        }
        printf("\n");
    }
}


