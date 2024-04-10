#include <stdio.h>
// #include <conio.h>
struct employee {
    char emp_name[50];
    int emp_id;
    int age;
    float salary;
};

int main() {
    struct employee emp;
    // clrscr();
    printf("Enter employee name: ");
    scanf("%s", emp.emp_name);
    printf("Enter employee ID: ");
    scanf("%d", &emp.emp_id);
    printf("Enter employee age: ");
    scanf("%d", &emp.age);
    printf("Enter employee salary: ");
    scanf("%f", &emp.salary);

    printf("\nEmployee Details:\n");
    printf("Name: %s\n", emp.emp_name);
    printf("ID: %d\n", emp.emp_id);
    printf("Age: %d\n", emp.age);
    printf("Salary: %.2f\n", emp.salary);
    // getch();
    return 0;
}
