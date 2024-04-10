package lessons;
import jdk.jfr.Description;

import java.util.ArrayList;
import java.util.Scanner;
public class l33 {
    static Scanner sc = new Scanner(System.in);

    static void isPresent(int[] arr, int idx, int x){
        if(idx==arr.length){
            System.out.println("No");
            return;
        }else if(arr[idx]==x){
            System.out.println("Yes");
            return;
        }
        isPresent(arr, idx+1, x);
    }

    static void findIdx(int[] arr, int idx, int x){
        if(idx>=arr.length){
            return;
        }
        if(arr[idx]==x){
            System.out.print(" "+idx+" ");
        }
        findIdx(arr, idx+1, x);
    }

    static ArrayList<Integer> printIdx(int[] arr, int idx, int x){
        ArrayList<Integer> ans = new ArrayList<>();
        if(idx>= arr.length) return ans;
        if(arr[idx]==x){
            ans.add(idx);
        }
//        ArrayList<Integer> smallAns =

        ans.addAll(printIdx(arr, idx+1, x));
        return ans;
    }

    static boolean isSorted(int[] arr, int idx){
        if(idx== arr.length-1){
            return true;
        }
        if(arr[idx]>arr[idx+1]){
            return false;
        }
        return isSorted(arr, idx+1);
    }

    static void lastIndex(int[] arr, int idx, int x){
        if(idx<0){
            System.out.println("Not found");
            return;
        }
        if(arr[idx]==x){
            System.out.println(idx);
            return;
        }
        lastIndex(arr, idx-1, x);
    }

    public static void main(String[] args) {

        int[] arr = {1, 2, 12, 64, 53, 42, 17, 89, 1, 4};
//        isPresent(arr, 0, 6);
//        ArrayList<Integer> ans = printIdx(arr, 0, 1);
//        System.out.println(ans);

        if(isSorted(arr, 0)){
            System.out.println("Sorted");
        } else {
            System.out.println("Not sorted");
        }

//        lastIndex(arr, arr.length-1, 5);


    }
}




