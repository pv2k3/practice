package newQuestions;

import java.util.Scanner;
public class pr7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        String[] arr1 = str.split(" ");
        int[] arr1LenElement = new int[arr1.length];
        for (int i = 0; i < arr1.length; i++) {
            arr1LenElement[i] = arr1[i].length();
        }
        boolean ch = false;
        for (int i = 0; i < arr1LenElement.length-1; i++) {
            if (arr1LenElement[i+1] == arr1LenElement[i]+1 ) ch = true;
            else break;
        }
        if(ch) System.out.println("IT IS A SNOWBALL STRING");
        else System.out.println("IT IS NOT A SNOWBALL STRING");
    }
}
