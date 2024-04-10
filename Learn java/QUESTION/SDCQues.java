package QUESTION;
import java.util.Scanner;
public class SDCQues {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of test cases");
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            System.out.println("Enter amount Alex has :");
            int a = sc.nextInt();
            System.out.println("Enter amount Bob has :");
            int b = sc.nextInt();
            System.out.println("Enter amount Charlie has :");
            int c = sc.nextInt();
            System.out.println("Enter amount needed to take subscription :");
            int x = sc.nextInt();

            if (a+b >=x || a+c >= x || b+c >= x){
                System.out.println("YES");
            }
            else {
                System.out.println("NO");
            }
        }
    }
}
