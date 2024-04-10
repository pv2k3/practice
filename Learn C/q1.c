#include <stdio.h>

void main(){
    int num1, num2, val, hcf, lcm = 1;
    printf("\n\n\n\n\n");
    printf("Enter two numbers :");
    scanf("%d %d", &num1, &num2);
    
    val = (num1 > num2) ? num1:num2;
    for (int i = 2; i <= val; i++){
        if(num1 % i ==0 && num2 % i ==0) hcf = i;
    }
    while(1){
        if(val%num1==0 && val%num2==0) {
            lcm = val;
            break;
        };
        ++val;
    }
    printf("%d is the greatest  common divisor\n", hcf);
    printf("%d is the lcm", lcm);
    printf("\n\n\n\n");
}