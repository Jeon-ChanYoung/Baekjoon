package Java;

import java.util.Scanner;

public class J7677 {
    static final int mod = 10000;

    static long[][] pow(long[][] A, long n) {
        if (n == 1) {
            return A;
        }
        long[][] x = pow(A, n / 2);
        if (n % 2 == 0) {
            return multi(x, x);
        } else {
            return multi(multi(x, x), A);
        }
    }

    static long[][] multi(long[][] A, long[][] B) {
        long x1 = (A[0][0]*B[0][0] + A[0][1]*B[1][0]) % mod;
        long x2 = (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % mod;
        long x3 = (A[1][0]*B[0][0] + A[1][1]*B[1][0]) % mod;
        long x4 = (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % mod;
        long[][] result = {{x1,x2}, {x3,x4}};
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long[][] A = {{1,1}, {1,0}};

        while (true) {
            long n = sc.nextLong();
            if (n == 0) {
                System.out.println(0);
                continue;
            } 
            if (n == -1) break;
            long[][] result = pow(A, n); 
            System.out.println(result[0][1]);
        }
    }
}
