package QUESTION;

import java.util.Scanner;

public class SwapValueWithoutThird {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.println("Value of a and b before swapping is : ");

        a = a^b;
        b = a^b;
        a = a^b;
        System.out.println("Value of a and b after swapping is : " + a +b);
    }
}
