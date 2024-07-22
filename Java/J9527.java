package Java;

import java.util.Scanner;

public class J9527 {
    static long[] prefix_sum = new long[60];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long A = sc.nextLong();
        long B = sc.nextLong();

        prefix_sum[0] = 0;
        for (int i = 1; i < 60; i++) {
            prefix_sum[i] = (1L << (i - 1)) + 2 * prefix_sum[i - 1];
        }

        long result = solve(B) - solve(A - 1);
        System.out.println(result);

        sc.close();
    }

    static long solve(long x) {
        String binary = Long.toBinaryString(x);
        int length = binary.length();
        long count = 0;

        for (int i = 0; i < length; i++) {
            if (binary.charAt(i) == '1') {
                int square = length - i - 1;
                count += prefix_sum[square] + x - (1L << square) + 1; 
                x -= (1L << square);
            }
        }
        return count;
    }
}
