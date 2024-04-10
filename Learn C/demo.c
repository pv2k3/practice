#include <stdio.h>

typedef struct{
    char Name[20];
    int rollNo;
    long callNumber;
} Student;
void f(){
    
}
int main()
{
    Student Priyanshu;
    Priyanshu.rollNo = 15;
    Priyanshu.callNumber = 9984178425;
    printf("%d", Priyanshu.rollNo);
    return 0;
}
