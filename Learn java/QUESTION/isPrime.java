package QUESTION;
import java.util.Scanner;

public class isPrime {
    public static void main() {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int count = 0;
        for (int i = 1; i <= num; i++) {
            if (num % i ==0) count++;
        }
        if (count == 2) System.out.println("The given number is prime");
        else System.out.println("The given number is not prime");


    }
}
