#include <stdio.h>

void convertToWords(int num) {
    char *one[] = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                   "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
    char *ten[] = {"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};

    if (num >= 10000000) {
        convertToWords(num / 10000000);
        printf(" Crore ");
        num %= 10000000;
    }

    if (num >= 100000) {
        convertToWords(num / 100000);
        printf(" Lakh ");
        num %= 100000;
    }

    if (num >= 1000) {
        convertToWords(num / 1000);
        printf(" Thousand ");
        num %= 1000;
    }

    if (num >= 100) {
        convertToWords(num / 100);
        printf(" Hundred ");
        num %= 100;
    }

    if (num > 0) {
        if (num < 20) {
            printf("%s ", one[num]);
        } else {
            printf("%s ", ten[num / 10]);
            if (num % 10 > 0) {
                printf("%s ", one[num % 10]);
            }
        }
    }
}

int main() {
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    if (num < 1 || num > 999999999) {
        printf("Please enter a number between 1 and 999999999.\n");
        return 1;
    }

    printf("Output: ");
    convertToWords(num);

    return 0;
}
