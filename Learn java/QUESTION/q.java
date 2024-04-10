package QUESTION;
import java.util.Scanner;

public class q {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        int len = line.length();
        int count = 0, min = 1000;;

        for (int i = 0; i < len; i++) {
            char ele = line.charAt(i);
            if (ele>='a' && ele<='z' || ele>='A' && ele<='Z') {
                if (i<len-1){
                    count++;
                }else{
                    count++;
                    if(min > count && count != 0){
                        min = count;
                    }
                }
            } else{
                if(min > count && count != 0){
                    min = count;
                }
                count = 0;
                continue;
            }

        }
        System.out.println(min);
    }
}
