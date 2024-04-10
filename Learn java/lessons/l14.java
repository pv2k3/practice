package lessons;
import java.util.Arrays;

class arrExample{
    public static void demoArrays(){
        String[][] age = {{"1","5","6"},{"31","3"},{"31","43","12"}};
        for (String[] num : age) {
            for (String a : num) {
                System.out.print(a + " ");
            }
            System.out.println();
        }

        System.out.println("Length of array"+ Arrays.deepToString(age) + age.length);
    }

}
class problems{
    static int add(int[] arr){  // Time complexity O(n)
        int sum = 0;
        for (int a:arr) {
            sum += a;
        }
        return sum;
    }
    static int max(int[] arr){
        int greater = 0;
        for (int a:arr) {
            if (a>greater){
                greater = a;
            }
        }
        return greater;
    }
    static int find(int[] arr,int val){
        int ch = -1;
        for(int i =0; i < arr.length; i++){
            if (arr[i] == val){
                ch = i;
                break;
            }
        }
        if (ch != -1) return ch;
        else return ch;
    }
}

public class l14 {
    public static void main(String[] args) {
//        arrExample.demoArrays();
        int[] a = {19,24,123,94,35,16,57,18,19,39,10};
//        System.out.println(problems.add(a));
//        System.out.println(problems.max(a));
        System.out.println(problems.find(a,19));
    }
}
