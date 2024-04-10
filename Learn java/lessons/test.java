package lessons;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import lessons.selfMadeMethod.*;
class reverse{
    static int[] swapArr(int[] arr , int i, int j){
        while (i<j){
            arr[i] = arr[i]^arr[j];
            arr[j] = arr[i]^arr[j];
            arr[i] = arr[i]^arr[j];
            i++;
            j--;
        }
        return arr;
    }

    void rev(ArrayList<Integer> ls, int l, int r){
        while(l<r){
            ls.set(l, ls.get(l)^ ls.get(r));
            ls.set(r, ls.get(l)^ ls.get(r));
            ls.set(l, ls.get(l)^ ls.get(r));
            l++;
            r--;
        }
    }
}
public class test {
    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        System.out.println("Enter the length of array");
//        int len = sc.nextInt();
//        int[] arr = new int[len];
//        selfMadeMethod.oneBasedMakeArray(arr,len);
//        System.out.println("Enter the number o times you want to rotate the array");
//        int rotate = sc.nextInt();
//
//        rotate = rotate % len;
//
//        reverse.swapArr(arr,0,len-rotate-1);
//        reverse.swapArr(arr,len-rotate,len-1);
//        reverse.swapArr(arr,0,len-1);
//
//        System.out.println(Arrays.toString(arr) );
//        int q = sc.nextInt();
//        int[] test = new int[1000];
//        for (int i = 0; i < len; i++) {
//            test[arr[i]] +=1;
//        }
//        for (int i = 0; i < q; i++) {
//            int a = sc.nextInt();
//            if(test[a] > 0) System.out.println("Present");
//            else System.out.println("Not Present");
//        };

        ArrayList<Integer> seq = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            seq.add(i);
        }
        System.out.println(seq);
        reverse obj = new reverse();
        obj.rev(seq, 0, seq.size()-1);

        System.out.println(seq);

    }
}
