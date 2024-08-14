package Java;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class J14562 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int C = sc.nextInt();
        for(int t=0; t<C; t++) {
            int S = sc.nextInt();
            int T = sc.nextInt();
            Deque<int[]> Q = new ArrayDeque<>();
    
            Q.add(new int[] { S, 0, T });
    
            while (!Q.isEmpty()) {
                int[] info = Q.pop();
                int pos = info[0];
                int count = info[1];
                int score = info[2];
    
                if (pos == score) {
                    System.out.println(count);
                    break;
                }
    
                if (pos < score) {
                    Q.add(new int[]{pos*2, count+1, score+3});
                    Q.add(new int[]{pos+1, count+1, score});
                }
            }
        }
    }
}
