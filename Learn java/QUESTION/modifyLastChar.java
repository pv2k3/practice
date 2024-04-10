package QUESTION;
import java.util.*;

public class modifyLastChar {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a word: ");
        String str = sc.nextLine().toLowerCase()+" ";
        int c=0;
        String nstr = "";String s="";
        int len = str.length();
        for (int i = 0; i < len; i++) {
            char ch=str.charAt(i);
            if(ch!=' ') {
                s=s+ch;
                c++;
            } else {
                char t=s.charAt(c-1);
                if(t=='a') {
                    nstr += s.substring(0,c-1)+'z'+" ";
                    c=0;
                } else {
                    nstr += s.substring(0,c-1)+(--t)+" ";
                    c=0;
                }
                s="";
            }
        }
        System.out.println(nstr);
    }
}

