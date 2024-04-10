package QUESTION;
import java.util.Scanner;
public class checkVowelInAString {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        int count = 0;
        for (int i = 0; i< line.length(); i++){
            char ch = line.charAt(i);
            if(ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u'){
                count++;
            }
        }
        if (count!=0) System.out.println("There are "+count+" vowels in line");
        else System.out.println("There are no vowels in the line");
    }
}
