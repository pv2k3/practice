package QUESTION;
import java.util.Scanner;

import lessons.selfMadeMethod;
import lessons.selfMadeMethod.*;
public class spiralExplore {
    static void spiral(int[][] arr, int r, int c){
        int rStart = 0, rEnd = r, cStart = 0, cEnd = c;
        int count = 0;
        while(count < r*c){
            for (int i = cStart; i<cEnd; i++){
                System.out.print(arr[rStart][i]+" ");
                ++count;
            }
            for (int i = rStart+1; i < rEnd; i++) {
                System.out.print(arr[i][cEnd-1]+" ");
                ++count;
            }
            for (int i = cEnd-2; i >= cStart; i--) {
                System.out.print(arr[rEnd-1][i]+" ");
                ++count;
            }
            for (int i = rEnd-2; i > rStart; i--) {
                System.out.print(arr[i][cStart]+" ");
                ++count;
            }
            rStart++;
            cStart++;
            rEnd--;
            cEnd--;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter size of matrix");
        int r = sc.nextInt();
        int c = sc.nextInt();

        int[][] arr = new int[r][c];
        selfMadeMethod.make2dArray(arr,r,c);
        spiral(arr,r,c);

    }
}
