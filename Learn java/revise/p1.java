package revise;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class p1 {
    static void swap(int[] arr, int j,int  k){
        int tmp;
        tmp = arr[j];
        arr[j] = arr[k];
        arr[k] = tmp;
//        return arr;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = {1,2,3};
        swap(arr, 0, 2);
        System.out.println(Arrays.toString(arr));
    }
}
