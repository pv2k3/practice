package QUESTION;

public class factorial {
    public static void fact(int n){
        int num = 1;
        for (int i = 2; i <= n; i++) {
            num *= i;
        }
        System.out.println("Factorial of the given number is : "+num);
    }
    public static void main(String[] args) {
        fact(6);
    }
}
