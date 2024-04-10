package QUESTION;
import java.util.Scanner;

class pythonToJava {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a word: ");
        String str = sc.nextLine().toLowerCase();
        String newstr = "";
        char nc=' ';
        int len = str.length();
        for (int i = 0; i < len; i++)
        {
            char ch = str.charAt(i);;
            if (ch == 'a' ||ch == 'e' ||ch == 'i' ||ch == 'o' ||ch == 'u')
            {
                nc = (char)(ch + 1);
                newstr = newstr + nc;
            }
            else
            {
                if(ch=='y')
                    nc='a';
                else if(ch=='z')
                    nc='b';
                else
                    nc = (char)(ch + 2);
                newstr=newstr + nc;
            }

        }
        System.out.println(newstr);
    }
}