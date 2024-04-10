package reviseEverything;
import java.util.Scanner;
public class numberConversion {
    public static int decimalToBinary(int n){
        int num = 0;
        int inc = 10;
        while (n>0){
            num += (n%2)*inc;
            n /= 2;
            inc*=10;
        }
        num /= 10;
        return num;
    }
    public static int binaryToDecimal(int n){
        int num = 0;
        int i =1;
        while(n>0){
            num += (n%10)*i;
            n/=10;
            i*=2;
        }
        return num;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
//        int n = sc.nextInt();
//        System.out.println("Binary num of the given number is :"+decimalToBinary(n));
//        System.out.println("Decimal num of given binary is :"+binaryToDecimal(n));
        System.out.println(12345/10000);
        System.out.println(12345%10000);

    }

}
