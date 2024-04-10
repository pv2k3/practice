package lessons;
import java.util.Scanner;

public class l30 {
    static int pow(int p, int q){
        if(q==0) return 1;
        if(q%2==0) return pow(p,q/2) * pow(p, q/2);
        return p * pow(p, q/2) * pow(p, q/2);
    }

    static void kMultiples(int num , int k){
        if(k<1){
            System.out.println("Invalid operation");
            return;
        } if(k==1) {
            System.out.println(num);
            return;
        }
        kMultiples(num, k-1);
        System.out.println(num*k);
    }

    static int Sum(int n){
        if(n==0) return 0;
        return n+Sum(n-1);
    }

    static int alterSum(int n){
        if(n==0) return 0;
        else if (n%2==1) {
            return alterSum(n-1)+n;
        }
        return alterSum(n-1)-n;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
//        int k = sc.nextInt();
//        System.out.println(pow(7, 3));
//        kMultiples(num, k);
        System.out.println(alterSum(num));
    }
}
