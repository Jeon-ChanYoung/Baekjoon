package Java;

import java.util.Scanner;

public class J17182 {
    static int N, K, MIN;
    static boolean[] visit;
    static int[][] graph;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        K = sc.nextInt();
        MIN = 999999999;
        visit = new boolean[N];
        graph = new int[N][];

        for (int i = 0; i < N; i++) {
            int[] temp = new int[N];
            for (int j = 0; j < N; j++) {
                temp[j] = sc.nextInt();
            }
            graph[i] = temp;
        }

        for(int k=0; k<N; k++) {
            for(int a=0; a<N; a++) {
                for(int b=0; b<N; b++) {
                    graph[a][b] = Math.min(graph[a][b], graph[a][k] + graph[k][b]);
                }
            }
        }
        backtracking(K, 0);
        System.out.println(MIN);
    }

    static void backtracking(int node, int cost) {
        if (allvisit()) {
            MIN = Math.min(MIN, cost);
            return;
        }

        for (int next = 0; next < N; next++) {
            if (!visit[next]) {
                visit[next] = true;
                backtracking(next, cost + graph[node][next]);
                visit[next] = false;
            }
        }
    }

    static boolean allvisit() {
        for(boolean isTrue : visit) {
            if (!isTrue) return false;
        }
        return true;
    }
}
