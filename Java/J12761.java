package Java;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class J12761 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int N = sc.nextInt();
        int M = sc.nextInt();
        boolean[] visit = new boolean[100001];
        visit[N] = true;

        Deque<int[]> Q = new ArrayDeque<>();
        int[] dx = {-1, 1, -A, -B, A, B, A, B};
        int[] bias = {0, 0, 0, 0, 0, 0, 1, 1};
        Q.add(new int[] { N, 0 });

        while (!Q.isEmpty()) {
            int[] info = Q.pop();
            int pos = info[0];
            int count = info[1];

            if (pos == M) {
                System.out.println(count);
                break;
            }

            for (int i = 0; i < 8; i++) {
                int next = pos * bias[i] * dx[i] + (pos + dx[i]) * (1 - bias[i]);
                if (0 <= next && next <= 100000 && !visit[next]) {
                    visit[next] = true;
                    Q.add(new int[] { next, count + 1 });
                }
            }
        }
    }
}
