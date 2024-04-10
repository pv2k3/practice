// To find the first number greater than 1000 in fabonicci series
package newQuestions;
import java.util.Scanner;
import lessons.selfMadeMethod.*;

public class q1 {
    public int fabAfterNth(int n){
        int a=0;
        int b=1;
        int sum=1;
        while(true){
            int tmp = a+b;
            a = b;
            b = tmp;
            sum+=tmp;
            if(tmp>n){
                System.out.println("--"+sum+"--");
                return tmp;
            }
        }
    }
    public static void main(String[] args) {
        q1 a = new q1();
        int n = 1000;
        System.out.println(a.fabAfterNth(n));
    }
}
