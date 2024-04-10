package newQuestions;
import java.util.Scanner;

class answer1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double calcTax=0;
        System.out.println("Enter your age");
        int age = sc.nextInt();
        System.out.println("Enter your Gender male/female");
        String gender = sc.next();
        System.out.println("Enter Taxable Amount");
        int taxableIncome = sc.nextInt();
        if (age<=65 && gender.equalsIgnoreCase("male")){
            if(taxableIncome<=160000){
                System.out.println("Tax calculated is NILL");
            }
            else if(taxableIncome<=500000){
                calcTax=(taxableIncome-160000)*0.1;
            }
            else if(taxableIncome<=800000){
                calcTax = ((taxableIncome-500000)*0.2)+34000;
            }
            else{
                calcTax = ((taxableIncome-800000)*0.3)+94000;
            }
        }
        else{
            System.out.println("Wrong category");
        }
        System.out.println("Tax calculated is "+calcTax);
    }
}