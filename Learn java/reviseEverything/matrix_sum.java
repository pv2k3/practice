package reviseEverything;
import java.util.Arrays;
import java.util.Scanner;

class methods{
    static Scanner sc = new Scanner(System.in);
    public static void makeArr(int[][] arr){
        int r = arr.length;
        int c = (r>0)? arr[0].length : 0;
        if (c==0) {
            System.out.println("Error");
            return;
        }
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
    }
    public static void matrixSum(int[][] arr1, int r1, int c1, int[][] arr2, int r2, int c2){
        if (r1 != r2 || c1!=c2){
            System.out.println("Addition not possible");
            return;
        }
        int[][] res = new int[r1][c1];
        for (int i = 0; i < r1; i++) {
            for (int j = 0; j < c1; j++) {
                res[i][j] = arr1[i][j] + arr2[i][j];
            }
        }
        for (int i = 0; i < r1; i++) {
            System.out.println(Arrays.toString(res[i]));
        }
    }
}

public class matrix_sum extends methods{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of rows and columns in array 1");
        int r1 = sc.nextInt();
        int c1 = sc.nextInt();
        int[][] arr1 = new int[r1][c1];
        makeArr(arr1);
        System.out.println("Enter the number of rows and columns in array 2");
        int r2 = sc.nextInt();
        int c2 = sc.nextInt();
        int[][] arr2 = new int[r2][c2];
        makeArr(arr2);
        matrixSum(arr1, r1, c1, arr2, r2, c2);
    }
}
