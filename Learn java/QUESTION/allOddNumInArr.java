package QUESTION;
import java.util.Scanner;

public class allOddNumInArr {
    public static void oddNum(int[] x){
        int count = 0;
        for (int i = 0; i < x.length; i++) {
            if (x[i]%2==0){
                count++;
            }
        }
        if (count ==0){
            System.out.println("All odd numbers");
        }
        else{
            System.out.println("All numbers are not odd");
        }
    }

}
