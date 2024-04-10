#include <stdio.h>

void main(){
    int val, rev = 0, count = 0;
    printf("Enter a number :");
    scanf("%d", &val);
    while(val>0){                        //Reverse the number 
        rev = rev*10 + val%10;
        val /= 10;
        count++;
    }
    while (1){                             //Read individual digits
        if (rev%10==0 && count !=0) printf("Zero ");  
        if (rev==0){
            break;
        }
        else if (rev%10==1) printf("One ");
        else if (rev%10==2) printf("Two ");
        else if (rev%10==3) printf("Three ");
        else if (rev%10==4) printf("Four ");
        else if (rev%10==5) printf("Five ");
        else if (rev%10==6) printf("Six ");
        else if (rev%10==7) printf("Seven ");
        else if (rev%10==8) printf("Eight ");
        else if (rev%10==9) printf("Nine ");
        rev /= 10;
        count--;
    }
}