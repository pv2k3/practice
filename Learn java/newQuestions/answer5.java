package newQuestions;
import java.util.Scanner;
public class answer5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter two numbers");
        int num1 = sc.nextInt();
        int num2 = sc.nextInt();
        int sum1 = 1;
        int sum2 = 1;

        for (int i = 2; i <= Math.sqrt(num1); i++) {
            if (num1 % i == 0) {
                sum1 += i;
                if (i != num1 / i) {
                    sum1 += num1 / i;
                }
            }
        }
        for (int i = 2; i <= Math.sqrt(num2); i++) {
            if (num2 % i == 0) {
                sum2 += i;
                if (i != num2 / i) {
                    sum2 += num2 / i;
                }
            }
        }
        if(sum1 == num2 && sum2 == num1) System.out.println("The numbers are amicable numbers");
        else System.out.println("The numbers are not amicable");

    }
}
