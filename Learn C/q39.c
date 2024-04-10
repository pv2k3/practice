    #include <stdio.h>

    void swap(int*, int*);

    void main(){
        int a, b;
        printf("Enter the value of a and b : ");
        scanf("%d %d", &a, &b);
        printf(" \nThe value before swapping is\n");
        printf(" a -- %d", a);
        printf(" b --  %d", b);
        swap(&a, &b);
        printf(" \nThe value after calling the swapping fuction inside the main function\n");
        printf(" a -- %d", a);
        printf(" b --  %d", b);
    }

    void swap(int *a, int *b){
        *a = *a + *b;
        *b = *a - *b;
        *a = *a - *b;
    }