package newQuestions;
import java.util.Scanner;

public class answer6 {
    void Tech_number(){
        for (int num = 1000; num <= 9999; num++) {
            int firstHalf = num / 100;
            int secondHalf = num % 100;

            int sum = firstHalf + secondHalf;
            int squareOfSum = sum * sum;

            if (squareOfSum == num) {
                System.out.println(num + " is a four digits Tech number.");
            }
        }
    }
    void pronic_number(){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number to check if it's a Pronic number: ");
        int pronicNum = sc.nextInt();

        boolean isPronic = false;

        for (int i = 1; i <= Math.sqrt(pronicNum); i++) {
            if (i * (i + 1) == pronicNum) {
                isPronic = true;
                break;
            }
        }

        if (isPronic) {
            System.out.println(pronicNum + " is a Pronic number.");
        } else {
            System.out.println(pronicNum + " is not a Pronic number.");
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        answer6 obj = new answer6();
        int choice;

        do {
            System.out.println("Menu:");
            System.out.println("\t1. Generate and print four digits Tech number");
            System.out.println("\t2. Check and print if a number is a Pronic number");
            System.out.println("\t3. Exit");
            System.out.print("\tEnter your choice (1-3): ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    obj.Tech_number();
                    break;
                case 2:
                    obj.pronic_number();
                    break;
                case 3:
                    System.out.println("Exiting the program. Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice. Please enter a number between 1 and 3.");
            }
        } while (choice != 3);
    }
}
