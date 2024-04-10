#include <stdio.h>
// #include <conio.h>

unsigned int invert(unsigned int x, int p, int n) {
    unsigned int mask = ((1u << n) - 1) << p-1;

    unsigned int result = x ^ mask;

    return result;
}

int main() {
    unsigned int x, result;
    int p, n;
    // clrscr();
    printf("\n\n");
    printf("Enter a number ");
    scanf("%u", &x);
    printf("Enter no. of bits to invert ");
    scanf("%d", &n);
    printf("Enter the position ");
    scanf("%d", &p);

    result = invert(x, p, n);
    printf("%u\n", result);
    // getch();
    return 0;
}
