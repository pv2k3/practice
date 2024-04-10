package lessons;
import java.util.Scanner;

public class l31 {
    static int gcdRecur(int n, int m){
        if(m == 0) return n;
        return gcdRecur(m, n%m);
    }
    static int lcm(int n, int m){
        return (n*m)/gcdRecur(n,m);
    }


    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
        System.out.println(lcm(15, 12));
    }
}
