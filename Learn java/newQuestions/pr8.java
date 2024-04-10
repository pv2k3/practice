package newQuestions;
import java.util.Scanner;
public class pr8 {

    static String changeChar(String s){
        if(s.length()==0){
            return "";
        }
        char current = s.charAt(0);
        String remaining = s.substring(1);
        if(current!=' ' && current!='z'){
            current = (char)(current+1);
        }else if(current=='z'){
            current = 'a';
        }
        return current+changeChar(remaining);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a line : ");
        String line = sc.nextLine();
        System.out.println(changeChar(line));
    }
}
