package Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;

/**
 * J14496
 */
public class J14496 {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input1 = br.readLine().split(" ");
        String[] input2 = br.readLine().split(" ");
        int a = Integer.parseInt(input1[0]);
        int b = Integer.parseInt(input1[1]);
        int N = Integer.parseInt(input2[0]);
        int M = Integer.parseInt(input2[1]);

        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for(int i=0; i<N+1; i++) {
            graph.add(new ArrayList<>());
        }

        for(int j=0; j<M; j++) {
            String[] input3 = br.readLine().split(" ");
            int A = Integer.parseInt(input3[0]);
            int B = Integer.parseInt(input3[1]);
            graph.get(A).add(B);
            graph.get(B).add(A);
        }
        
        boolean[] visit = new boolean[N+1];
        visit[a] = true;

        Deque<int[]> Q = new ArrayDeque<>();
        Q.add(new int[]{a, 0});

        while (!Q.isEmpty()) {
            int[] info = Q.pop();
            int node = info[0];
            int count = info[1];

            if (node == b) {
                System.out.println(count);
                System.exit(0);
            }

            for(int next : graph.get(node)) {
                if (!visit[next]) {
                    visit[next] = true;
                    Q.add(new int[]{next, count+1});
                }
            }
        }
        System.out.println(-1);
    }
}