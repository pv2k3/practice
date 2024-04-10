package lessons;
import java.util.Scanner;
import lessons.selfMadeMethod.*;

public class l21 {
    static void transposeMatrix(int[][] arr, int r, int c){
        int[][] newArr = new int[c][r];
        for (int i = 0; i < c; i++) {
            for (int j = 0; j < r; j++) {
                newArr[i][j] = arr[j][i];
            }
        }
        selfMadeMethod.print2dArray(newArr);
    }
    static void rotateMatrixClockWise90(int[][] arr, int r, int c){
        int[][] newArr = new int[c][r];
        for (int i = 0; i < c; i++) {
            int val =0;
            for (int j = r-1; j >= 0; j--) {
                newArr[i][val] = arr[j][i];
                val++;
            }
        }
        selfMadeMethod.print2dArray(newArr);
    }
    static void pascalTriangle(int n){
        int[][] arr = new int[n][];
        for (int i = 0; i < n; i++) {
            arr[i] = new int[i+1];
            for (int j = 0; j <= i; j++) {
                if (j == 0 || j == i) {
                    arr[i][j] = 1;
                }
                else{
                    arr[i][j] = arr[i-1][j]+arr[i-1][j-1];
                }
            }
        }
        selfMadeMethod.print2dArray(arr);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of rows and columns :");
        int r = sc.nextInt();
        int c = sc.nextInt();
        int[][] arr = new int[r][c];
        selfMadeMethod.make2dArray(arr,r,c);
//        transposeMatrix(arr,r,c);
        rotateMatrixClockWise90(arr,r,c);
//        System.out.println("Enter no. of lines");
//        int n = sc.nextInt();
//        pascalTriangle(n);
    }
}
