package newQuestions;
import java.util.Scanner;

public class answer4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter serial number ");
        int srNo = sc.nextInt();
        System.out.print("Enter Name ");
        String name = sc.nextLine();
        System.out.print("Enter ticket charges ");
        double tkCharge = sc.nextDouble(); // Changed to nextDouble for decimal input
        double discount, netAmount;

        if (tkCharge <= 25000)
            discount = 2;
        else if (tkCharge <= 35000)
            discount = 10;
        else if (tkCharge <= 55000)
            discount = 12;
        else if (tkCharge <= 70000)
            discount = 16;
        else
            discount = 18;

        netAmount = tkCharge - (tkCharge * (discount / 100)); // Corrected the calculation
        System.out.println("Sr. No.\tName\tTicket charges\tDiscount\tNet amount");
        System.out.println(srNo + "\t" + name + "\t" + tkCharge + "\t" + discount + "\t" + netAmount);
    }
}

