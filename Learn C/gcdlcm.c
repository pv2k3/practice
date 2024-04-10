#include <stdio.h>
// #include <conio.h>

int hcf(int, int);
int lcm(int, int);

int main(){
	int num1, num2, HCF, LCM;
	// clrscr();
	printf("Enter two numbers :");
	scanf("%d %d", &num1, &num2);
	HCF = hcf(num1, num2);
	LCM = lcm(num1, num2);
	printf("%d is the greatest common divisor\n", HCF);
	printf("%d is the lcm", LCM);
	// getch();
    return 0;
}

int hcf(int num1, int num2){
    int val, i, HCF=0;
	val = (num1 < num2)? num1:num2;
    for (i = 2; i <= val; i++){
		if(num1 % i ==0 && num2 % i ==0) HCF = i;
	}
    return HCF;
}
int lcm(int num1, int num2){
    int LCM=0;
    LCM = (num1*num2)/hcf(num1, num2);
    return LCM;
}