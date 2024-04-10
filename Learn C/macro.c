#include <stdio.h>
// #include <conio.h>
#define min(a,b) ((a<b)?a:b)
#define max(a,b) ((a>b)?a:b)

int main(){
    int a, b, c;
    int d, e, f;
    // clrscr();
    printf("Enter two numbers : ");
    scanf("%d%d", &a,&b);
    c = min(a,b);
    printf("The min value between %d and %d is %d\n", a, b, c);
    printf("Enter two numbers : ");
    scanf("%d%d", &d,&e);
    f = max(d,e);
    printf("The max value between %d and %d is %d\n", d, e, f);
    // getch();
    return 0;
}