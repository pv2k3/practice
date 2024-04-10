#include <stdio.h>
#include <math.h>

int isPrimeNo(int n){
    int count = 0;
    for (int i = 1; i <= n; i++){
        if(n%i==0) count++; 
    }
    return count == 2;
}
int isCompositeNo(int n){
    int count = 0;
    for (int i = 1; i <= n; i++){
        if(n%i==0) count++;
    }
    return count != 2;
    
}
int isPerfectNumber(int num) {
    int sum = 1;
    for (int i = 2; i * i <= num; ++i) {
        if (num % i == 0) {
            sum += i;  
            if (i * i != num) {
                sum += num / i;
            }
        }
    }
    return sum == num;
}

int isNeonNum(int n){
    int sum = 0, dummy = n;
    n *= n;
    while(n>0){
        sum+=n%10;
        n /= 10;
    }
    return sum==dummy;
}

int isPalindrome(int n){
    int rev = 0, dummy = n;
    while(n>0){
        rev = rev*10 + n%10;
        n /= 10;
    }
    return rev == dummy;
}

int isArmstrong(int n){
    int dummy = n, arm = 0;
    while(n>0){
        int digit = n%10;
        arm += (int)pow(digit,3);
        n /= 10;
    }
    return arm == dummy;
}
int main() {
    int n;
    printf("Enter a number : ");
    scanf("%d", &n);
    if (isArmstrong(n)){
        printf("The number is Armstrong number");
    }
    else{
        printf("The number is not a Arrmstrong Number");
    }
    return 0;
}
