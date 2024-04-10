package QUESTION;
import java.util.Scanner;

public class vowelFrequency {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        int[] count = new int[5];
        for (int i = 0; i < line.length(); i++) {
            char val = line.charAt(i);
            if (val == 'a'){
                count[0]++;
            } else if (val == 'e') {
                count[1]++;
            }else if (val == 'i') {
                count[2]++;
            }else if (val == 'o') {
                count[3]++;
            }else if (val == 'u') {
                count[4]++;
            }
        }
        System.out.println("Frequency of a is : "+count[0]);
        System.out.println("Frequency of e is : "+count[1]);
        System.out.println("Frequency of i is : "+count[2]);
        System.out.println("Frequency of o is : "+count[3]);
        System.out.println("Frequency of u is : "+count[4]);
    }
}
