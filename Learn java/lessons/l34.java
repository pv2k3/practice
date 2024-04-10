package lessons;
import java.util.Scanner;

public class l34 {
    static Scanner sc = new Scanner(System.in);

    static String removeElement(String str, char c){
        if(str.length()==0) return "";
        String smallAns = removeElement(str.substring(1), c);
        char current = str.charAt(0);
        if(current!=c){
            return current+smallAns;
        } else {
            return smallAns;
        }
    }

    static String reverseString(String str){
        if(str.length()==0) return "";
        return reverseString(str.substring(1)) + str.charAt(0);
    }

    static boolean isPalindrome(String s, int l, int r){
        if(l>=r) return true;
        if(s.charAt(l)!=s.charAt(r)){
            return false;
        }
        return (isPalindrome(s, l+1, r-1));
    }

    static boolean isPalindrome2(String s){
        if(s.length()==0 || s.length()==1) return true;
        if(s.charAt(0)!=s.charAt(s.length()-1)) return false;
        return isPalindrome2(s.substring(1, s.length()-1));
    }

    public static void main(String[] args) {
//        System.out.println("Enter a line ");
//        String line = sc.nextLine();
//        System.out.println("Enter char to remove");
//        char word = sc.next().charAt(0);
//        System.out.println(removeElement(line, word));
        String line = sc.nextLine();
//        System.out.println(reverseString("aaa"));

        if(isPalindrome2(line)){
            System.out.println("Is palindrome");
        }else {
            System.out.println("Not palindrome");
        }

    }
}
