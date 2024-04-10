#include <stdio.h>

int main(){
    int n, i, sm, ssm;
    int arr[50];
    printf("Enter the size of the 1d matrix : ");
    scanf("%d", &n);
    printf("Enter elements\n");
    for(i=0; i<n; i++){
        scanf("%d", &arr[i]);
    }
    sm = arr[0];
    for(i=0; i<n; i++){
        if(arr[i]<sm) sm = arr[i];
    }
    ssm = arr[0];
    for(i=0; i<n; i++){
        if (arr[i]==sm) continue;
        else if(arr[i]<ssm) ssm = arr[i];
    }
    printf("The second smallest elemenet is %d", ssm);
    return 0;
}