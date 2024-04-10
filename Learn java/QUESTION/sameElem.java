package QUESTION;

import java.util.Arrays;
import java.util.Scanner;

public class sameElem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] a = {9, 8, 7, 6, 5, 4, 3, 2, 1};
        int[] b = {9, 8, 7, 6, 5, 4, 3, 2, 1};
        if (Arrays.equals(a, b)) System.out.println("The elements are same");
    }
}
