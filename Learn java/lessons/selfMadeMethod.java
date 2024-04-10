package lessons;
import java.util.Arrays;
import java.util.Scanner;

public class selfMadeMethod {
    public static void printArray(int[] a){
        for (int val: a) {
            System.out.print(val + " ");
        }
    }
    public static void printArray(String[] a){
        for (String val: a) {
            System.out.print(val + " ");
        }
    }
    public static int[] zeroBasedMakeArray(int[] arr,int len){
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < len; i++) {
            arr[i] = sc.nextInt();
        }
        return arr;
    }
    public static String[] zeroBasedMakeArray(String[] arr,int len){
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < len; i++) {
            arr[i] = sc.nextLine();
        }
        return arr;
    }
    public static int[] oneBasedMakeArray(int[] arr,int len){
        Scanner sc = new Scanner(System.in);
        for (int i = 1; i <= len; i++) {
            arr[i] = sc.nextInt();
        }
        return arr;
    }
    public static String[] oneBasedMakeArray(String[] arr,int len){
        Scanner sc = new Scanner(System.in);
        for (int i = 1; i <= len; i++) {
            arr[i] = sc.nextLine();
        }
        return arr;
    }
    public static int[] reverseArr(int[] arr , int i, int j){
        while (i<j){
            arr[i] = arr[i]^arr[j];
            arr[j] = arr[i]^arr[j];
            arr[i] = arr[i]^arr[j];
            i++;
            j--;
        }
        return arr;
    }
    public static int totalSum(int[] arr){
        int sum = 0;
        for (int ele:arr) {
            sum+=ele;
        }
        return sum;
    }
    public static int[] rotateNonTemp(int[] arr, int k){
        int len = arr.length;
        reverseArr(arr, 0, len - k - 1);
        reverseArr(arr, len - k, len - 1);
        reverseArr(arr, 0, len - 1);
        System.out.println(Arrays.toString(arr));
        return arr;
    }
    public static int[][] make2dArray(int[][] arr, int len1, int len2){
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < len1; i++) {
            for (int j = 0; j < len2; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        return arr;
    }
    public static String[][] make2dArray(String[][] arr, int len1, int len2){
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < len1; i++) {
            for (int j = 0; j < len2; j++) {
                arr[i][j] = sc.nextLine();
            }
        }
        return arr;
    }
    public static int[][] make2dJaggedArray(int[][] arr, int len1){
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < len1; i++) {
            System.out.println("Enter no. of columns in row "+i);
            int col = sc.nextInt();
            for (int j = 0; j < col; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        return arr;
    }
    public static String[][] make2dJaggedArray(String[][] arr, int len1){
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < len1; i++) {
            System.out.println("Enter no. of columns in row "+i);
            int col = sc.nextInt();
            for (int j = 0; j < col; j++) {
                arr[i][j] = sc.nextLine();
            }
        }
        return arr;
    }
    public static void print2dArray(int[][] arr){
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
    }
    public static void print2dArray(String[][] arr){
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
    }
}
