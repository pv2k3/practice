package QUESTION;
import java.util.Scanner;

public class fibonacciRecursion {

    public static void recur(int n){
        int a = 0;
        int b = 1;
        int c;
        System.out.print(a+" ");
        for (int i = 0; i < n-1; i++) {
            c = a;
            a = b;
            b = c+a;
            System.out.print(a+" ");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the length of the fabonicci series");
        int num = sc.nextInt();

        recur(num);
    }
}
