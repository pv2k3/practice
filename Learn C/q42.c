#include <stdio.h>

void main(){
	int n, val, check=0, i;
	int arr[50];
	printf("\nEnter length of array :");
	scanf("%d", &n);
    printf("Enter elements");
    for(i=0; i<n; i++){
		scanf("%d", &arr[i]);
	}
	printf("\nEnter the value you want to search :");
	scanf("%d", &val);
	for(i=0; i<n; i++){
		if(arr[i]==val){
			printf("Element %d found in array at index %d", val, i);
			check = 1;
			break;
		}
	}
	if(check==0) printf("Element %d not found in array", val);

}