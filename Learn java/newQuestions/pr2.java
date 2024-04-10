package newQuestions;
import java.util.*;

public class pr2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number :");
        int num = sc.nextInt();
        int count = 0;
        for (int i = num; i > 0; i /= 10) {
            count++;
        }

        int result = 0;

        if(count%2==0){
            for (int i = num; i > 0 ; i /= 10) {
                result = result*10 + i%10;
            }
            System.out.println(result);
        }
        else {
            int a = (count/2)+1;
            int b = (int)Math.pow(10, a);
            int c = b*10;
            int d = b/10;
            result = (num/b * d) + num%d;
            System.out.println(result);
        }



    }

}
