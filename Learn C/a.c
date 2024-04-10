#include<stdio.h>
#include<math.h>

int main(){
	int a, b, c, d;
	printf("Enter the value of a :");
	scanf("%d", &a);
	printf("Enter the value of b :");
	scanf("%d", &b);
	printf("Enter the value of c :");
	scanf("%d", &c);
	d = pow(b,2)-(4*a*c);
	if(d<0) {
		printf("Imaginary roots");
	}
	else if(d==0) {
		printf("Root are equal and  %d",-b/(2*a));
	}
	else {
		printf("Roots are %f  %f",(-b+pow(d,0.5))/(2*a),(-b-pow(d,0.5))/(2*a));
	}
	return 0;
}

