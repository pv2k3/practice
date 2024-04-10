package lessons;
import java.util.Scanner;
import lessons.selfMadeMethod.*;

public class l22 {
    static void spiralTraversal(int[][] arr,int r,int c){
        int endr = r, endc = c;
        int strr = 0, strc = 0, count = 0;
        while(count < r*c){
            for (int i = strc; i < endc; i++) {
                System.out.print(arr[strr][i]+" ");
                ++count;
            }
            for (int i = strr+1; i < endr; i++) {
                System.out.print(arr[i][endc-1]+" ");
                ++count;
            }
            for (int i = endc-2; i >= strc ; i--) {
                System.out.print(arr[endr-1][i]+" ");
                ++count;
            }
            for (int i = endr-2; i > strr ; i--) {
                System.out.print(arr[i][strc]+" ");
                ++count;
            }
            endr--;
            endc--;
            strr++;
            strc++;
        }
    }
    static void makeSpiralArray(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of rows and columns");
        int r = sc.nextInt();
        int c = sc.nextInt();
        int[][] arr = new int[r][c];
        int endr = r, endc = c;
        int strr = 0, strc = 0, count = 1;
        while(count <= r*c){
            for (int i = strc; i < endc; i++) {
                arr[strr][i] = count++;
            }
            for (int i = strr+1; i < endr; i++) {
                arr[i][endc-1] = count++;
            }
            for (int i = endc-2; i >= strc ; i--) {
                arr[endr-1][i] = count++;
            }
            for (int i = endr-2; i > strr ; i--) {
                arr[i][strc] = count++;
            }
            endr--;
            endc--;
            strr++;
            strc++;
        }
        selfMadeMethod.print2dArray(arr);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of rows and columns");
        int r = sc.nextInt();
        int c = sc.nextInt();
        int[][] arr = new int[r][c];
        selfMadeMethod.make2dArray(arr,r,c);
        spiralTraversal(arr,r,c);
//        makeSpiralArray();

    }
}
