package lessons;
import lessons.selfMadeMethod.*;

import java.util.Arrays;
import java.util.Scanner;
public class l15 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter length of array");
        int len = sc.nextInt();
        int[] ar = new int[len];
        selfMadeMethod.oneBasedMakeArray(ar,len);
//        problems1(ar);
//        System.out.println("Enter value to find");
//        int val = sc.nextInt();
//        problem2(ar,val);
//        Arrays.sort(ar);
//        System.out.println(Arrays.toString(ar));
    }

    public static void problems1(int[] arr){
        System.out.println("Enter val to find");
        Scanner sc = new Scanner(System.in);
        int count = 0;
        int valToFind = sc.nextInt();
        for (int val:arr) {
            if(val == valToFind){
                count ++;
            }
        }
        System.out.println("No. of occurrences : " + count);
    }
    public static void problem2(int[] arr, int val){
        int ind = 0;
        for(int i = 0; i < arr.length; i++){
            if (arr[i] == val) ind = i;
        }
        System.out.println("The last occurrence of given value is on " +ind);
    }
    public static void problem3(int[] arr){
        int ind = 0;
        for(int i = 0; i < arr.length; i++){
            if (arr[i] > ind) ind = arr[i];
            else{
                System.out.println("NotSorted");
                break;
            }
        }
        if (ind == arr.length) {
            System.out.println("Sorted");
        }

    }
}
