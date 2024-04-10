package lessons;
import java.util.Scanner;
import java.util.Arrays;
import lessons.selfMadeMethod.*;



public class l17 {
    public static void swap(int a, int b){
        System.out.println("Value before swapping ");
        System.out.println("a : "+a);
        System.out.println("b : "+b);
        a = a^b;
        b = a^b;
        a = a^b;
        System.out.println("Value before swapping ");
        System.out.println("a : "+a);
        System.out.println("b : "+b);
    }
    static int[] reverseArr(int[] arr , int i, int j){
        while (i<j){
            arr[i] = arr[i]+arr[j];
            arr[j] = arr[i]-arr[j];
            arr[i] = arr[i]-arr[j];
            i++;
            j--;
        }
        return arr;
    }
    static void rotateNonTemp(int[] arr, int k){
        int len = arr.length;
        reverseArr(arr, 0, len - k - 1);
        reverseArr(arr, len - k, len - 1);
        reverseArr(arr, 0, len - 1);
        System.out.println(Arrays.toString(arr));

    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter length of array");
        int len = sc.nextInt();
        int[] arr = new int[len];
        selfMadeMethod.zeroBasedMakeArray(arr,len);
        int[] dummyArr = new int[len];
        System.out.println("Enter the number of times to rotate");
        int k = sc.nextInt();
        k = k%len;
//        int pos = 0;
//        for (int i = len-k; i < arr.length; i++) {
//            dummyArr[pos++] = arr[i];
//        }
//        for (int i = 0; i < len-k; i++) {
//            dummyArr[pos++] = arr[i];
//        }
//        System.out.println(Arrays.toString(dummyArr));
//        System.out.println(Arrays.toString(swapArr(arr, 0, len - 1)));
        rotateNonTemp(arr,k);
    }
}
