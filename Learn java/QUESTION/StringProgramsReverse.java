package QUESTION;

import java.util.Scanner;

public class StringProgramsReverse {
    public static void main() {
        Scanner sc = new Scanner(System.in);

        String val = sc.next();
        char[] a = val.toCharArray();
        String rev = "";

        for (int i = val.length()-1; i >=0 ; i--) {
            rev += a[i];
        }
        System.out.println(rev);
    }
}