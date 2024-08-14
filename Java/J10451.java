package Java;

import java.util.Scanner;

public class J10451 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-->0) {
            int N = sc.nextInt();
            int count = 0;
            int[] graph = new int[N];
            boolean[] visit = new boolean[N];

            for(int i=0; i<N; i++) {
                graph[i] = sc.nextInt()-1;
            }

            for(int i=0; i<N; i++) {
                if (!visit[i]) {
                    int temp = i;
                    count++;
                    while (true) {
                        int next = graph[temp];
                        visit[temp] = true;
                        if (visit[next]) {
                            break;
                        }
                        temp = next;
                    }
                }
            }
            System.out.println(count);
        }
    }
}
