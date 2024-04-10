package lessons;
import java.util.Arrays;
import java.util.Scanner;
import lessons.selfMadeMethod.*;
import java.lang.Math;
class problemsSolve{
    public static void p1() {
        int[] arr = {10,8,9,15,7,1,2,4,13,17,19,32,21,3};
        int max1 = 0;
        int max2 = 0;
        for(int i :arr){
            if(i>max1) max1 =i;
        }
        for (int i:arr) {
            if(i>max2 && i!=max1) max2 =i;
        }
        System.out.println("Second largest number is: "+max2);
    }
    public static void pr2(int[] arr){
        int ch = 0;
        for(int i =0; i<arr.length-1;i++){
            for(int j = i+1;j<arr.length;j++){
                if(arr[i]==arr[j]){
                    System.out.println(arr[i]);
                    ch = 1;
                    break;
                }
            }
            if(ch == 1) break;
        }
        if(ch ==0) System.out.println(-1);
    }

}

public class l16 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Len");
        int len = sc.nextInt();
//        int[] arr =new int[len];
//        selfMadeMethod.makeArray(arr,len);
//        System.out.println("Sum val to find");
//        int val = sc.nextInt();
//        int count = 0;
//        for (int el1:arr) {
//            for (int el2:arr) {
//                if (el1 + el2 == val)count++;
//            }
//        }
//        System.out.println(count/2);
//        System.out.println(Arrays.stream(arr).count());
//
//
//        problemsSolve.p1();
//        problemsSolve.pr2(arr);
    }
}
