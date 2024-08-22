package Java;

import java.util.Arrays;
import java.util.Scanner;

/**
 * J1679
 */
public class J1679 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] numbers = new int[N];
        int[] DP = new int[50001];
        for(int i=0; i<N; i++) {
            numbers[i] = sc.nextInt();
        }
        int K = sc.nextInt();
        Arrays.fill(DP, 9999999);
        Arrays.sort(numbers);
        DP[0] = 0;

        for(int num : numbers) {
            for(int i=num; i<50001; i++) {
                DP[i] = Math.min(DP[i], DP[i-num]+1);
            }
        }
        
        for(int i=0; i<50001; i++) {
            if (DP[i] > K) {
                String result = i%2==0 ? "holsoon" : "jjaksoon";
                System.out.println(result + " win at " + i);
                break; 
            }
        }
    }
}