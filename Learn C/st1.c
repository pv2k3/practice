#include <stdio.h>

struct employee{
    char *emp_name[50];
    int emp_id;
    int age;
    float salary;
};


int main(){
    struct employee e1;
    printf("Enter Employee Name : ");
    scanf("%s", &e1.emp_name);
    printf("Enter Employee Id : ");
    scanf("%d", &e1.emp_id);
    printf("Enter Employee Age : ");
    scanf("%d", &e1.age);
    printf("Enter Employee Salary : ");
    scanf("%f", &e1.salary);

    printf("Employee : %s", e1.emp_name);
    printf("Id : %d", e1.emp_id);
    printf("Age : %d", e1.age);
    printf("Salary : %f", e1.salary);
}