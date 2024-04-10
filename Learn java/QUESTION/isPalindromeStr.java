package QUESTION;
import java.util.Scanner;
public class isPalindromeStr {
    public static void isPalindrome(String val){
        val = val.toLowerCase();
        int l = 0;
        int r = val.length()-1;
        char[] iter = val.toCharArray();
        while (l <= r){
            if (iter[l] != iter[r]){
                System.out.println("The given string is not palindrome");
                break;
            }
            l += 1;
            r -= 1;
        }
        System.out.println("Is palindrome");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        isPalindrome(a);
    }
}
