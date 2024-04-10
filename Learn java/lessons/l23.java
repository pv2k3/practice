package lessons;
import java.util.Scanner;
import lessons.selfMadeMethod.*;

public class l23 {

    public static void makePrefixSumArray2d(int[][] arr){
        int r = arr.length;
        int c = arr[0].length;
        for (int i = 0; i < r; i++) {
            for (int j = 1; j < c; j++) {
                arr[i][j] += arr[i][j-1];
            }
        }
        for (int i = 1; i < r; i++) {
            for (int j = 0; j < c; j++) {
                arr[i][j] += arr[i-1][j];
            }
        }
    }

    public static int sumRange2d(int[][] arr, int l1, int r1, int l2, int r2){
        int ans = 0;

        if (l1 > 0 && r1 > 0){
            int sum = arr[l2][r2];
            int up = arr[l1-1][r2];
            int left = arr[l2][r1-1];
            int leftup = arr[l1-1][r1-1];
            ans = sum - up - left + leftup;
        } else if (l1 > 0 && r1 == 0) {
            ans = arr[l2][r2] - arr[l1-1][r2];
        } else if (l1 == 0 && r1 > 0) {
            ans = arr[l2][r2] - arr[l2][r2-1];
        }else if (l1 == 0 && r1 == 0){
            ans = arr[l2][r2];
        }


        return ans;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of rows and columns");
        int r = sc.nextInt();
        int c = sc.nextInt();
        int[][] arr = new int[r][c];
        selfMadeMethod.make2dArray(arr, r, c);

        makePrefixSumArray2d(arr);

        selfMadeMethod.print2dArray(arr);

        System.out.println("Enter value of l1 r1 and l2 r2");
        int l1 = sc.nextInt();
        int r1 = sc.nextInt();
        int l2 = sc.nextInt();
        int r2 = sc.nextInt();

        System.out.println("Sum is : "+ sumRange2d(arr, l1, r1, l2, r2));

    }
}
