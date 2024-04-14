package revise;

import java.util.Arrays;
import java.util.Scanner;
import revise.*;
public class p3 {
    static Scanner sc = new Scanner(System.in);
    p2 obj = new p2();
    static void bubbleSort(int[] arr ){
        int len = arr.length;
        for (int i = 0; i < len-1; i++) {
            boolean flag = false;
            for (int j = 0; j < len-i-1; j++) {
                if(arr[j]>arr[j+1]){
                    p2.swap(arr, j, j+1);
                    flag = true;
                }
            }
            if(!flag){
                break;
            }
        }
    }
    static void selectionSort(int[] arr){
        int len = arr.length;
        for (int i = 0; i < len-1; i++) {
            int min = i;
            for (int j = i+1; j < len; j++) {
                if(arr[min] > arr[j]){
                    min = j;
                }
            }
            p2.swap(arr, i, min);
        }
    }
    static void insertionSort(int[] arr){
        int len = arr.length;
        for (int i = 1; i < len; i++) {
            int j = len-1;
            while(j!=0 && j >= i){
                if(arr[j-1] > arr[j]){
                    p2.swap(arr, j, j-1);
                }
                j--;
            }
        }
    }
    public static void main(String[] args) {
        System.out.println("Enter the length of array ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        p2.makeArr(arr, n);
//        bubbleSort(arr);
//        selectionSort(arr);
        insertionSort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
