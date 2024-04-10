#include <stdio.h>


int main(){
    int decimalNumber, binaryNumber;
    printf("\n\n\n");
    printf("Enter a decimal number : ");
    scanf("%d", &decimalNumber);
    int num = 1;
    while (decimalNumber >0){
        binaryNumber = binaryNumber + (decimalNumber%2)*num;
        decimalNumber /= 2;
        num *= 10;
    }
    printf("Binary Number for the given number %d is %d", decimalNumber, binaryNumber);
    printf("\n\n\n");
    return 0;
}