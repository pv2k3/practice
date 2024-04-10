#include <stdio.h>
#include <conio.h>

void main(){
	int monthNum;
	clrscr();
	printf("Enter the month number");
	scanf("%d", &monthNum);
	switch (monthNum){
		case 1:
			printf("31 days in month : %d", monthNum);
			break;
		case 2:
			printf("28 days in month : %d", monthNum);
			break;
		case 3:
			printf("31 days in month : %d", monthNum);
			break;
		case 4:
			printf("30 days in month : %d", monthNum);
			break;
		case 5:
			printf("31 days in month : %d", monthNum);
			break;
		case 6:
			printf("30 days in month : %d", monthNum);
			break;
		case 7:
			printf("31 days in month : %d", monthNum);
			break;
		case 8:
			printf("31 days in month : %d", monthNum);
			break;
		case 9:
			printf("30 days in month : %d", monthNum);
			break;
		case 10:
			printf("31 days in month : %d", monthNum);
			break;
		case 11:
			printf("30 days in month : %d", monthNum);
			break;
		case 12:
			printf("31 days in month : %d", monthNum);
			break;
		default:
			break;
		}
	getch();
}