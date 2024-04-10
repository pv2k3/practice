#include <stdio.h>
#include <math.h>

int main(){
    float l, b, h;
    float area, volume, spaceDagonals;
    printf("\n\n\n\n\n");
    printf("Enter the values of length : ");
    scanf("%f", &l);
    printf("Enter the values of breadth : ");
    scanf("%f", &b);
    printf("Enter the values of height : ");
    scanf("%f", &h);
    area = 2*(l*b + b*h + h*l);
    volume = l*b*h;

    spaceDagonals = sqrt(pow(l,2)+pow(b,2)+pow(h,2));
    
    printf("Area : %0.2f\n", area);
    printf("Volume : %0.2f\n", volume);
    printf("Space Diagonals : %0.2f\n", spaceDagonals);
    printf("\n\n\n\n");
    return 0;
}
