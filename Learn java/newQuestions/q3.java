package newQuestions;

public class q3 {
    public boolean isPrime(int n){
        int count = 0;
        for(int i = 1; i <= n; i++){
            if (n%i == 0) count++;
        }
        if(count==2) return true;
        else return false;
    }
    public static void main(String[] args) {
        q3 a = new q3();
        int n = 600;
        for (int i = 2; i < n; i++) {
            if (a.isPrime(i)) System.out.print(i+" ");
        }
    }
}
