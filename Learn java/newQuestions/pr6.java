package newQuestions;
import java.util.Scanner;

public class pr6 {
    static Scanner sc = new Scanner(System.in);
    public static void make2DArray(float[][] arr, int n){
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                float val = sc.nextFloat();
                if(val<0){
                    System.out.println("Invalid entry");
                }
                else{
                    arr[i][j] = val;
                }
            }
        }
    }
    public static void main(String[] args) {
        int n = sc.nextInt();
        float[][] arr = new float[n][n];
        make2DArray(arr, n);
        boolean isDoublyMarkov = true;
        for (int i = 0; i < n; i++) {
            float a = 0;
            float b = 0;
            for (int j = 0; j < n; j++) {
                a+=arr[i][j];
                b+=arr[j][i];
            }
            if (a==1 && b==1){
                continue;
            }
            else{
                isDoublyMarkov = false;
                break;
            }
        }
        System.out.println(isDoublyMarkov);
    }
}
