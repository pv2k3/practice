#include <stdio.h>
int main()
{
	int num, count= 0;
	printf("Enter a number : ");
	scanf("%d", &num);
	for (int i = 0; i < num; i++){
		if(num % i == 0){
			count++;
		}
	}
	if(count==2){
		printf("The entered number is Prime number.");
	}
	else{
		printf("The entered number is not prime.");
	}
	
	
	return 0;
}
