package lessons;

import java.security.spec.RSAOtherPrimeInfo;
import java.util.Arrays;
import java.util.Scanner;
import lessons.selfMadeMethod.*;

public class l19p2 {
    static int equalSumPartition(int[] arr){
        int totalSum = selfMadeMethod.totalSum(arr);
        int prefixSum = 0;
        for (int i = 0; i < arr.length; i++) {
            prefixSum += arr[i];
            int suffixSum = totalSum - prefixSum;
            if(prefixSum==suffixSum){
                return i;
            }
        }
        return -1;
    }
    static int[] slicedArray(int[] arr,int l, int r){
        int[] dummy = new int[r-l+1];
        int v = 0;
        for (int i = l; i <= r; i++) {
            dummy[v++] = arr[i];
        }
        return dummy;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("len");
        int len = sc.nextInt();
        int[] arr = new int[len];
        selfMadeMethod.zeroBasedMakeArray(arr,len);
        int a = equalSumPartition(arr);
        if (a!=-1){
            System.out.println(Arrays.toString(slicedArray(arr,0,a)));
            System.out.println(Arrays.toString(slicedArray(arr,a+1, arr.length-1)));
        }
        else System.out.println("Not found");
    }
}
