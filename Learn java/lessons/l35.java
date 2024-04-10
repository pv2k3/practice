package lessons;
import java.util.*;
public class l35 {
    static Scanner sc = new Scanner(System.in);

    static ArrayList<String> getSSQ(String s){
        ArrayList<String> ans = new ArrayList<>();
        if(s.length()==0){
            ans.add("");
            return ans;
        }
        char current = s.charAt(0);
        ArrayList<String> smallAns = getSSQ(s.substring(1));

        for(String ss: smallAns){
            ans.add(ss);
            ans.add(current+ss);
        }
        return ans;
    }

    static void getSSQ2(String s, String currAns){
        if(s.length()==0){
            System.out.println(currAns);
            return;
        }

        char current = s.charAt(0);
        String smallAns = s.substring(1);


        getSSQ2(smallAns, currAns+current);
        getSSQ2(smallAns, currAns);
    }

    static void getSSQSum(int[] arr, int idx, int sum){
        if(idx==arr.length){
            System.out.println(sum);
            return;
        }
        getSSQSum(arr, idx+1, sum+arr[idx]);
        getSSQSum(arr, idx+1, sum);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        getSSQSum(new int[]{1, 2, 3}, 0, 0);
    }
}
