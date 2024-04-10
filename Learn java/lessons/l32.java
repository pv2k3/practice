package lessons;
import java.security.spec.RSAOtherPrimeInfo;
import java.util.Scanner;

public class l32 {
    static void printArray(int[] arr, int idx){
        if(idx== arr.length-1){
            System.out.print(" "+arr[idx]+" ");
            return;
        }
        System.out.print(" "+arr[idx]+" ");
        printArray(arr, idx+1);
    }

    static int maxVal(int[] arr, int idx){
        if(idx== arr.length-1){
            return arr[idx];
        }
        if(arr[idx] > maxVal(arr, idx+1)){
            return arr[idx];
        }
        return maxVal(arr, idx+1);
    }

    static int sum(int[] arr, int idx){
        if(idx== arr.length-1) return arr[idx];
        return arr[idx] + sum(arr, idx+1);
    }

    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        printArray(new int[]{1, 2, 3, 4, 5, 6, 7}, 0);
        int[] arr = {1, 2, 12, 64, 53, 42, 17, 89, 1, 4};

        System.out.println("sum : "+ sum(arr, 0));
        System.out.println("Max value : "+ maxVal(arr, 0));
        printArray(arr, 0);
    }
}
