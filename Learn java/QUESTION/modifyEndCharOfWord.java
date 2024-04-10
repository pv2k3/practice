package QUESTION;
import java.util.Scanner;
public class modifyEndCharOfWord {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        int len = line.length();
        String nwString = "";
        for (int i = 0; i < len-1; i++) {
            if ((line.charAt(i+1) == ' ')){
                 if (line.charAt(i)=='a') nwString += 'z';
                 else nwString += (char)(line.charAt(i)-1);
            }
            else{
                nwString += line.charAt(i);             //correct
            }
        }
        if (line.charAt(len-1)=='a') nwString += 'z';
        else nwString += (char)(line.charAt(len-1)-1);
        System.out.println(nwString);
    }
}
