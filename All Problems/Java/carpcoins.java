import java.lang.Math;
import java.util.Scanner;

public class carpcoins {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        solution(n);
        sc.close();
    }

    public static void solution(int n){
        int a1;
        int a2;

        double c1 = 0;
        double c2 = 0;

        double q = n / 3;
        double r = n % 3;

        if (r == 0){
            c1 = n / 3;
            c2 = c1;
        }

        c1 = q;
        c2 = Math.round((n - c1) / 2);
        
        a1 = (int)c1;
        a2 = (int)c2;

        if(a1*1 + a2*2 != n){
            int t = a1;
            a1 = a2;
            a2 = t;
        }
        
        System.out.print(a1 + " " + a2);
        System.out.println();
    }
}