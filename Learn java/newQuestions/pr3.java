package newQuestions;
import java.util.*;
public class pr3 {
    public static void print(String n) {
        boolean isConsecutive = false;

        for (int i = 0; i < n.length() - 1; i++) {
            if ((n.charAt(i + 1) - n.charAt(i)) == 1) {
                isConsecutive = true;
                break;
            }
        }

        if (isConsecutive) {
            System.out.println("Yes, it is Consecutive String");
        } else {
            System.out.println("No, it is not Consecutive String");
        }
    }

    public static void print(int n) {
        boolean isUnique = isUniqueNumber(n);

        if (isUnique) {
            System.out.println("Yes, it is a Unique number");
        } else {
            System.out.println("No, it is not a Unique number");
        }
    }

    private static boolean isUniqueNumber(int num) {
        boolean[] visited = new boolean[10];

        while (num > 0) {
            int digit = num % 10;
            if (visited[digit]) {
                return false; // Digit repeated, not unique
            }

            visited[digit] = true;
            num /= 10;
        }

        return true; // All digits are unique
    }

    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        // Example 1
        String str = sc.next();
        print(str);

        // Example 2
        int num = sc.nextInt();
        print(num);
    }
}
