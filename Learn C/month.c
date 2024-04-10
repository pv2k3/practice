#include <stdio.h>

void main(){
    int monthNum;
    printf("\n\n\n");
    printf("Enter the month number");
    scanf("%d", &monthNum);
    if (monthNum<8){
        switch (monthNum%2)
        {
        case 1:
            printf("31 days in month : %d", monthNum);
            break;
        case 0:
            (monthNum==2)?printf("28 days in month : %d", monthNum):printf("30 days in month : %d", monthNum);
            break;
        default:
            break;
        }
    }
    else{
        switch (monthNum%2)
        {
        case 0:
            printf("31 days in month : %d", monthNum);
            break;
        case 1:
            printf("30 days in month : %d", monthNum);
            break;
        default:
            break;
        }
    }
    printf("\n\n\n\n");
}