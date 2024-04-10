package newQuestions;
import java.util.Scanner;
public class pr5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float p = 1, s = 1;
        float sum= 0;
        System.out.print("Num");
        int n = sc.nextInt();
        for (int i = 2; i <= n; i++) {
            p*=i;
            s+=i;
            sum += (p/s);
        }
        System.out.println(sum);
    }
}
