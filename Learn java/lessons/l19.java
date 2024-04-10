package lessons;

import java.util.Scanner;
import java.util.Arrays;
import lessons.selfMadeMethod.*;

public class l19 {

    static int[] prefixSum(int[] arr, int len){
        for (int i = 1; i < len; i++) {
            arr[i] = arr[i]+arr[i-1];
        }
        return arr;
    }
    static int[] suffixSum(int[] arr, int len){
        for (int i = len-2; i >= 0; i--) {
            arr[i] = arr[i]+arr[i+1];
        }
        return arr;
    }

    static void p2(int[] arr, int len){
        Scanner sc = new Scanner(System.in);
        prefixSum(arr,len);
        System.out.println("Enter the no. of queries");
        int q = sc.nextInt();
        for (int i = 0; i < q; i++) {
            System.out.println("Enter value of l and r");
            int l = sc.nextInt();
            int r = sc.nextInt();
            System.out.println(arr[r]-arr[l-1]);
        }
    }
    static void p3(int[] arr,int len){
        int c = 0;
        for (int i = 0; i < len-1; i++) {
            if(prefixSum(arr,len)[i] == suffixSum(arr,len)[i+1]){
                c++;
            }
        }
        if(c!=0) System.out.println(true);
        else System.out.println(false);
    }

    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        System.out.println("Enter the length of the array");
        int len = sc.nextInt();
        int[] arr = new int[len];
        selfMadeMethod.zeroBasedMakeArray(arr,len);
//        p2(arr,len);
//        suffixSum(arr,len);
//        selfMadeMethod.printArray(arr);
        p3(arr,len);
    }
}
