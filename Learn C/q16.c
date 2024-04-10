#include <stdio.h>

void main(){
    float mSub1, mSub2, mSub3, mSub4, mSub5, gp;
    printf("\n\n\n\n");
    printf("Enter your numbers in five papers out of 100\n");
    scanf("%f %f %f %f %f", &mSub1, &mSub2, &mSub3, &mSub4, &mSub5);
    gp = ((mSub1+mSub2+mSub3+mSub4+mSub5)/5)/10;
    if(gp<2) printf(" Your grade is F and grade point is %0.2f", gp);
    else if(gp<3) printf("Your grade is D and grade point is %0.2f", gp);
    else if(gp<3.50) printf("Your grade is C and grade point is %0.2f", gp);
    else if(gp<4) printf("Your grade is B and grade point is %0.2f", gp);
    else printf("Your grade is A and grade point is %0.2f", gp);
    printf("\n\n\n");
}