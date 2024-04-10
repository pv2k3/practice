#include <stdio.h>
#define PI 3.14

int main(){
	int dimension1, dimension2, choice;
	printf("Input a value from the choice below to choose\n");
	printf("\t1. Triangle\n\t2. Circle\n\t3. Rectangle\n\t4. Square\n");
	scanf("%d", &choice);
	if (choice == 1){	 
		printf("Enter the base and height of triangle : ");
		scanf("%d", &dimension1);
		scanf("%d", &dimension2);
		printf("Area of Triangle is %f", 0.5*dimension1*dimension2);
	}
	else if (choice == 2){ 
		printf("Enter the Radius of circle : ");
		scanf("%d",&dimension1);
		printf("Area of circle is %f", PI*dimension1*dimension1);
	}
	else if (choice == 3){ 
		printf("Enter the base and length of rectangle : ");
		scanf("%d", &dimension1);
		scanf("%d", &dimension2);
		printf("Area of Rectangle is %d", dimension1*dimension2);
	}
	else if (choice == 4){ 
		printf("Enter the Side of Square : ");
		scanf("%d",&dimension1);
		printf("Area of square is %d", dimension1*dimension1);
	}
	return 0;
}