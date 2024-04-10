#include <stdio.h>
// #include <conio.h>
struct student {
    char name[50];
    int roll_number;
    float percentage;
    char grade;
};

char calculateGrade(float percentage) {
    if (percentage >= 75.0) {
        return 'A';
    } else if (percentage >= 60.0) {
        return 'B';
    } else if (percentage >= 50.0) {
        return 'C';
    } else {
        return 'F';
    }
}

int main() {
    struct student s;
    // clrscr();
    printf("Enter details for the student:\n");
    printf("Name: ");
    scanf("%s", s.name);

    printf("Roll Number: ");
    scanf("%d", &s.roll_number);

    printf("Percentage: ");
    scanf("%f", &s.percentage);

    s.grade = calculateGrade(s.percentage);

    printf("\nStudent Details with Grade:\n");
    printf("Name: %s\n", s.name);
    printf("Roll Number: %d\n", s.roll_number);
    printf("Percentage: %.2f\n", s.percentage);
    printf("Grade: %c\n", s.grade);
    // getch();
    return 0;
}
