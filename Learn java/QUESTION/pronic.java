package QUESTION;
import java.util.Scanner;

public class pronic {
    private int num;
    public pronic() {
        num = 0;
    }
    public void acceptnum() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a positive integer number: ");
        num = scanner.nextInt();
    }
    public boolean isPronic(int v) {
        if (v == 0) return true;
        int i = 1;
        while (i * (i + 1) <= v) {
            if (i * (i + 1) == v) return true;
            i++;
        }
        return false;
    }
    public void check() {
        boolean result = isPronic(num);
        if (result) System.out.println(num + " is a pronic number.");
        else System.out.println(num + " is not a pronic number.");
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter no. of testcases");
        int n = sc.nextInt();
        pronic pronicObj = new pronic();
        for (int i = 0; i < n; i++) {
            pronicObj.acceptnum();
            pronicObj.check();
        }
    }
}

