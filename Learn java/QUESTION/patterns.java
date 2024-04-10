package QUESTION;

public class patterns {
    /*
            *
           ***
          *****
         *******
     */
    public static void triangle1(int n){
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < n-i; j++) {
                System.out.print(" ");
            }
            for (int k = 1; k <= 2*i-1; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
    /*
                *
               * *
              *   *
             *******
     */
    public static void triangle2(int n){
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n-i; j++) {
                System.out.print(" ");
            }
            for (int k = 1; k <= 2*i-1; k++) {
                if (i == 1 || i==n || k==1 || k== 2*i-1) {
                    System.out.print("*");
                }
                else{
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        triangle2(6);
    }
}
