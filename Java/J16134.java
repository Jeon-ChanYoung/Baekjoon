package Java;
import java.util.Scanner;

public class J16134 {

    static final int P = 1_000_000_007;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int R = sc.nextInt();

        long fN = factorial(N);
        long fNR = factorial(N - R);
        long fR = factorial(R);

        long result = fN * power(fNR * fR % P, P - 2) % P;
        System.out.println(result);
    }

    static long factorial(int n) {
        long total = 1;
        for (int i = 1; i <= n; i++) {
            total *= i;
            total %= P;
        }
        return total;
    }

    static long power(long a, int n) {
        if (n == 1) {
            return a % P;
        }
        long x = power(a, n / 2);
        x = (x * x) % P;
        if (n % 2 != 0) {
            x = (x * a) % P;
        }
        return x;
    }
}
