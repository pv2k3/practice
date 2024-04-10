package newQuestions;
import java.util.Scanner;
public class answer2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Bike number");
        int bikeNo = sc.nextInt();
        System.out.print("Phone number");
        String phoneNo = sc.next();
        System.out.print("Number of days");
        int days = sc.nextInt();
        int charge;

        if(days<=5) charge = 500*days;
        else if(days<=10) charge = 2500+(days-5)*400;
        else if(days<=20) charge = 2500+2000+(days-10)*300;
        else charge = 2500+2000+3000+(days-20)*200;

        System.out.println("Bike No.\tPhone No.\tNo. of days\tCharge");
        System.out.println(bikeNo+"\t"+phoneNo+"\t"+days+"\t"+charge);
    }
}
