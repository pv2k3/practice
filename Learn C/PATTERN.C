#include <stdio.h>
// #include <conio.h>
int main(){
    int n, i, j;
    // clrscr();
    printf("Enter the number of lines : ");
    scanf("%d", &n);
    for (i=1; i<=n; i++){
        for(j=1; j<=n-i; j++){
            printf(" ");
        }
        for(j=1; j<=i; j++){
            if(i==1 || j==1 || i==n || j==n){
                printf("%d", i);
            }else{
                printf(" ");
            }
        }
        for(j=i-1; j>0; j--){
            if(i==1 || j==1 || i==n || j==n){
                printf("%d", i);
            }else{
                printf(" ");
            }
        }
        printf("\n");
    }
    // getch();
    return 0;
}