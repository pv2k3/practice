package revise;
import java.util.Arrays;
import java.util.Scanner;
public class p2 {
    static Scanner sc= new Scanner(System.in);
    static void swap(int[] arr, int j,int  k){
        int tmp;
        tmp = arr[j];
        arr[j] = arr[k];
        arr[k] = tmp;
    }
    static void makeArr(int[] arr, int len){
        System.out.println("Enter elements : ");
        for (int i = 0; i < len; i++) {
            arr[i] = sc.nextInt();
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter size :");
        int len = sc.nextInt();
        int[] arr = new int[len];
        makeArr(arr, len);
        for (int i = 0; i < len-1; i++) {
            boolean flag = false;
            for (int j = 0; j < len-i-1; j++) {
                if(arr[j] > arr[j+1]){
                    swap(arr, j, j+1);
                    flag = true;
                }
            }
            if(!flag){
                System.out.println("reached break for i="+i);
                break;
            }
        }
        System.out.println(Arrays.toString(arr));
    }
}