package lessons;
import java.util.Scanner;

public class l27_28_29 {

    static void pi(int n){
        if(n==1){
            System.out.println(1);
            return;
        }
        else{
            pi(n-1);
            System.out.println(n);
        }
    }

    static int sum(int n){
        if(n==1) return n;
        else return n+sum(n-1);
    }

    static long factorial(int n) {
        if (n == 1) return n;
        else return n * factorial(n - 1);
    }

    static int sumDigit(int n){
        if(n>=0 && n<10) return n;
        else return (n%10) + sumDigit(n/10);
    }

    static int numOfDigit(int n){
        if(n>=0 && n<10) return 1;
        else return 1 + numOfDigit(n/10);
    }

    static long power(int a, int b){
        if(b==0) return 1;
        else return a*power(a, b-1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
//        System.out.println(sumDigit(a));
        System.out.println(numOfDigit(a));

    }
}
