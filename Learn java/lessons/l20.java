package lessons;

import java.util.Arrays;
import java.util.Scanner;

public class l20 {
    static void addMatrix(int[][] arr1, int r1, int c1, int[][] arr2, int r2, int c2){
        if (r1!=r2 || c1!=c2){
            System.out.println("Wrong input addition not possible");
            return;
        }
        int[][] sum = new int[r1][c1];

        for (int i = 0; i < r1; i++) {
            for (int j = 0; j < c1; j++) {
                sum[i][j] = arr1[i][j] + arr2[i][j];
            }
        }
        selfMadeMethod.print2dArray(sum);
    }
    static void multiplyMatrix(int[][] arr1, int r1, int c1, int[][] arr2, int r2, int c2){
        if (c1 != r2) {
            System.out.println("Wrong input array cannot be multiplied");
            return;
        }
        int[][] multiply = new int[r1][c2];

        for (int i = 0; i < r1; i++) {
            for (int j = 0; j < c2; j++) {
                for (int k = 0; k < c1; k++) {
                    multiply[i][j] += arr1[i][k]*arr2[k][j];
                }
            }
        }
//        selfMadeMethod.print2dArray(multiply);
        for (int i = 0; i < r1; i++) {
            System.out.println(Arrays.toString(multiply[i]));
        }
    }
    static void reverseEachRow(int[][] arr, int r, int c){
        int[][] newArr = new int[r][c];
        for (int i = 0; i <r ; i++) {
            int v = 0;
            for (int j = c-1; j >= 0; j--) {
                newArr[i][v] = arr[i][j];
                v++;
            }
        }
        selfMadeMethod.print2dArray(newArr);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter row");
        int r1 = sc.nextInt();
        System.out.println("Enter column");
        int c1 = sc.nextInt();
        int[][] arr1 = new int[r1][c1];
        selfMadeMethod.make2dArray(arr1,r1,c1);

        System.out.println("Enter row");
        int r2 = sc.nextInt();
        System.out.println("Enter column");
        int c2 = sc.nextInt();
        int[][] arr2 = new int[r2][c2];
        selfMadeMethod.make2dArray(arr2,r2,c2);

//        addMatrix(arr1,r1,c1,arr2,r2,c2);
        multiplyMatrix(arr1,r1,c1,arr2,r2,c2);
//        reverseEachRow(arr1,r1,c1);
    }
}
