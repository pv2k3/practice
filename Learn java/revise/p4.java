package revise;

import java.util.Scanner;

public class p4 {
    static void merge_sort(int[] arr, int l, int r){
        int len = arr.length;
        if(arr.length == 2){
            if(arr[l]>arr[r]){
                int tmp = arr[l];
                arr[l] = arr[r];
                arr[r] = tmp;
                return;
            }
        }
        if(arr.length==1){
            return;
        }


    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
    }
}
