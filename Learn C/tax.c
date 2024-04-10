#include <stdio.h>

int main(){
    int salary;
    float taxToBePaid;
    printf("\n\n");
    printf("Salary : ");
    scanf("%d", &salary);
    
    if (salary <= 5000){
        taxToBePaid = 0;
    }
    else if (salary > 5000 && salary <=15000){
        taxToBePaid = (salary-5000)*0.1;
    }
    else if (salary > 15000 && salary <= 35000){
        taxToBePaid = ((10000)*0.1) + ((salary-15000)*0.15);
    }
    else if (salary > 35000){
        taxToBePaid = ((10000)*0.1) + ((20000)*0.15) + ((salary-35000)*0.2);
    }
    
    printf("The tax amount to be paid is : %f", taxToBePaid);
    printf("\n\n\n\n\n");
    return 0;
}