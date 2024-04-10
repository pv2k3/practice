package QUESTION;

import java.util.Scanner;

public class Evil {
    private int num;
    private String bin;
    public Evil() {
        num = 0;
        bin = "";
    }
    public void acceptNum() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a positive integer number: ");
        num = scanner.nextInt();
    }
    public void rec_bin(int x) {
        if (x > 0) {
            rec_bin(x / 2);
            bin += Integer.toString(x % 2);
        }
    }
    public void check() {
        rec_bin(num);
        int countOnes = bin.replace("0", "").length(); // Counting the number of 1's in the binary representation

        if (countOnes % 2 == 0) System.out.println(num + " is an Evil number.");
        else System.out.println(num + " is not an Evil number.");
    }
    public static void main(String[] args) {
        Evil evilObj = new Evil();
        evilObj.acceptNum();
        evilObj.check();
    }
}
