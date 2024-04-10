package QUESTION;
import java.util.Scanner;

class DeciOct {
    private int n;
    private int Oct;
    private int change;
    public DeciOct() {
        n = 0;
        Oct = 0;
        change=10;
    }
    public void getnum(int nn) {
        n = nn;
    }
    private void deci_oct() {
        if (n != 0) {

            Oct += (n % 8)*change;
            change*=10;
//            Oct *= 10;
            n /= 8;
            deci_oct();
        }
    }
    public void show() {
        System.out.println("Decimal Number: " + n);
        deci_oct(); // Calculate octal equivalent
        Oct /= 10; // Adjust the extra factor of 10 from the last recursive call
        System.out.println("Octal Equivalent: " + Oct);
    }
}
public class Main {
    public static void main(String[] args) {
        DeciOct obj = new DeciOct();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a decimal number: ");
        int num = scanner.nextInt();
        obj.getnum(num);
        obj.show();
    }
}

