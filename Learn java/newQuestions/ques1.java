package newQuestions;
import java.util.Scanner;
public class ques1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            int c = i;
            for (int j = 1; j <= i; j++) {
                if(j%2==1){
                    System.out.print(c + "\t");
                    c += n-j;
                }
                else{
                    System.out.print(c + "\t");
                    c += n-j;
                }
            }
            System.out.println();
        }
    }
}
