package newQuestions;
import java.util.Arrays;
import java.util.Scanner;

import lessons.selfMadeMethod;
import lessons.selfMadeMethod.*;
public class q4 {
    static void sortInPlaceAscending(int[] arr,int n){
        for (int i = 0; i < n-1; i++) {
            for (int j = i+1; j < n; j++) {
                if (arr[i] > arr[j]) {
                    int tmp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = tmp;
                }
            }
        }
    }
    static void sortInPlaceDescending(int[] arr,int n){
        for (int i = 0; i < n-1; i++) {
            for (int j = i+1; j < n; j++) {
                if (arr[i] < arr[j]) {
                    int tmp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = tmp;
                }
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        selfMadeMethod.zeroBasedMakeArray(arr,n);
        System.out.println(Arrays.toString(arr));
        sortInPlaceAscending(arr,n);
        System.out.println(Arrays.toString(arr));
        sortInPlaceDescending(arr,n);
        System.out.println(Arrays.toString(arr));
    }
}
