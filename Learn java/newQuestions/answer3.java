package newQuestions;
import java.util.Scanner;
import java.util.Scanner;

public class answer3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice;

        do {
            System.out.println("Menu:");
            System.out.println("1. Check and display whether the number is an Abundant Number");
            System.out.println("2. Check and print whether the number is a Dudeney number");
            System.out.println("3. Exit");
            System.out.print("Enter your choice (1-3): ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter a number to check for Abundant Number: ");
                    int abundantNum = scanner.nextInt();
                    int sumOfFactors = 0;

                    for (int i = 1; i <= abundantNum / 2; i++) {
                        if (abundantNum % i == 0) {
                            sumOfFactors += i;
                        }
                    }

                    if (sumOfFactors > abundantNum) {
                        System.out.println(abundantNum + " is an Abundant Number.");
                    } else {
                        System.out.println(abundantNum + " is not an Abundant Number.");
                    }
                    break;
                case 2:
                    System.out.print("Enter a number to check for Dudeney Number: ");
                    int dudeneyNum = scanner.nextInt();

                    int sumOfDigits = 0;
                    int temp = dudeneyNum;

                    while (temp > 0) {
                        sumOfDigits += temp % 10;
                        temp /= 10;
                    }

                    int cubeRoot = (int) Math.cbrt(dudeneyNum);

                    if (sumOfDigits == cubeRoot) {
                        System.out.println(dudeneyNum + " is a Dudeney Number.");
                    } else {
                        System.out.println(dudeneyNum + " is not a Dudeney Number.");
                    }
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
