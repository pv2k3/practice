package newQuestions;
import java.util.Scanner;
public class pr4 {
    public static boolean isPrime(int n){
        int c = 0;
        for (int i = 1; i <= n; i++) {
            if(n%i==0) c++;
        }
        if (c == 2) return true;
        else return false;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        boolean isHamming  = false;
        for(int i = 2; i <= Math.sqrt(num); i++){
            if(num%i == 0 && i==2) isHamming = true;
            else if(num%i == 0 && i==3) isHamming = true;
            else if(num%i == 0 && i==5) isHamming = true;
            else if (num%i==0 && isPrime(i)) isHamming = false;
        }
        if(isHamming) System.out.println("The given number is a hamming number");
        else System.out.println("The given number is not a Hamming number");
    }
}
