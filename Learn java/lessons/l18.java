package lessons;

import java.util.Scanner;
import java.util.Arrays;
import lessons.selfMadeMethod.*;

import static java.lang.Math.abs;
import static java.lang.Math.pow;

public class l18 {

    static void sortZeroesMethod(int[] arr,int len){
        int left = 0;
        int right = len-1;
        while(right > left){
            if(arr[left]==1 && arr[right]==0){
                arr[left] = arr[left]^arr[right];
                arr[right] = arr[left]^arr[right];
                arr[left] = arr[left]^arr[right];
            }
            if (arr[left] == 0)left++;
            if (arr[right] == 1)right--;
        }
    }
    static void sortEvenOddMethod(int[] arr,int len){
        int left = 0;
        int right = len-1;
        while(right > left){
            if(arr[left]%2==1 && arr[right]%2==0){
                arr[left] = arr[left]^arr[right];
                arr[right] = arr[left]^arr[right];
                arr[left] = arr[left]^arr[right];
            }
            if (arr[left]%2 == 0)left++;
            if (arr[right]%2 == 1)right--;
        }
    }
    static int[] sortSqr(int[] arr, int len){
        int left = 0;
        int right = len-1;
        int[] ans = new int[len];
        int k = len-1;
        while(left <= right){
            if(abs(arr[left]) > abs(arr[right])){
                ans[k--] = arr[left]*arr[left];
                left++;
            }
            else{
                ans[k--] = arr[right]*arr[right];
                right--;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int len = sc.nextInt();
        int[] arr = new int[len];
        selfMadeMethod.zeroBasedMakeArray(arr,len);
//        sortZeroesMethod(arr,len);
//        sortEvenOddMethod(arr,len);
//        int[] a = sortSqr(arr,len);
        selfMadeMethod.printArray(arr);
    }
}
