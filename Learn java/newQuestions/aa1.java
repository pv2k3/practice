package newQuestions;

import java.util.*;
class aa1
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number of teams");
        int n = sc.nextInt();
        if(n<=2||n>=9)
        {
            System.out.println("Invalid Input");
            return;
        }
        String[] name = new String[n];
        int t=0;
        System.out.println("Enter the team names");
        for(int i=0; i<n; i++){
            name[i]=sc.nextLine();
            if(name[i].length()>t)  t=name[i].length();
        }
        for(int i=0;i<n;i++)
        {
            System.out.println("Team"+" "+(i+1)+" "+name[i]);
        }
        for(int i=0;i<t;i++){
            for(int j=0;j<n;j++){
                if(i>=name[j].length()){
                    System.out.print(' ');
                }
                else{
                    System.out.print(name[j].charAt(i));
                }
                System.out.print(" ");
            }
            System.out.println();
        }
    }
}