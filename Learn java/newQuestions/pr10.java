package newQuestions;
import java.util.*;
public class pr10 {
    static String modifyEndOfChar(String s){
        if (s.length()==1){
            return "";
        }
        char ch = s.charAt(0);
        String remaining = s.substring(1);
        if(s.charAt(1)==' '&&ch!='z'){
            ch=(char)(ch+1);
        } else if (s.charAt(1)==' '&&ch=='z') {
            ch = 'a';
        }
        return ch+(modifyEndOfChar(remaining));
    }

    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a line");
        String line = sc.nextLine()+" ";        // shift the char (char)curr+1
        System.out.println(modifyEndOfChar(line));
    }
}
