package Java;

import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.stream.IntStream;

public class J10021 {
    static int[] parent;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int C = sc.nextInt();
        int[][] temp = new int[N][];
        PriorityQueue<int[]> info = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        parent = IntStream.range(0, N).toArray();
        int total = 0;

        for(int i=0; i<N; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            temp[i] = new int[]{x,y};
        }

        for(int i=0; i<N; i++) {
            for(int j=i+1; j<N; j++) {
                int[] node1 = temp[i];
                int[] node2 = temp[j];
                int distance = (int)(Math.pow(node1[0] - node2[0], 2) + Math.pow(node1[1] - node2[1], 2));
                if (distance >= C) {
                    info.add(new int[]{distance, i, j});
                }
            }
        }

        while (!info.isEmpty()) {
            int[] nodeInfo = info.poll();
            int distance = nodeInfo[0];
            int A = nodeInfo[1];
            int B = nodeInfo[2];

            if (find(A) != find(B)) {
                union(A, B);
                total += distance;
            }
        }
        
        solve(total);
    }

    static int find(int node) {
        if (node != parent[node]) {
            parent[node] = find(parent[node]);
        }
        return parent[node];
    }

    static void union(int A, int B) {
        int root_A = find(A);
        int root_B = find(B);
        parent[Math.max(root_A, root_B)] = Math.min(root_A, root_B);
    }

    static void solve(int total) {
        for(int i : parent) {
            if (i != 0) {
                System.out.println(-1);
                return;
            }
        }
        System.out.println(total);
    }
}
