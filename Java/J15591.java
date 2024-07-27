package Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;

public class J15591 {
    static int N;
    static ArrayList<ArrayList<int[]>> graph = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int Q = Integer.parseInt(input[1]);

        for(int i=0; i<N+1; i++) {
            graph.add(new ArrayList<>());
        }

        for(int i=0; i<N-1; i++) {
            String[] video = br.readLine().split(" ");
            int p = Integer.parseInt(video[0]);
            int q = Integer.parseInt(video[1]);
            int r = Integer.parseInt(video[2]);
            graph.get(p).add(new int[]{q, r});
            graph.get(q).add(new int[]{p, r});
        }

        for(int i=0; i<Q; i++) {
            String[] question = br.readLine().split(" ");
            int k = Integer.parseInt(question[0]);
            int v = Integer.parseInt(question[1]);
            int answer = USADO(k, v);
            System.out.println(answer);
        }
    }

    static int USADO(int k, int v) {
        int total = 0;
        Deque<Integer> Q = new ArrayDeque<>();
        boolean[] visit = new boolean[graph.size()];
        visit[v] = true;

        Q.add(v);
        while (!Q.isEmpty()) {
            int node = Q.pop();
            for(int[] info : graph.get(node)) {
                int next_node = info[0];
                int value = info[1];
                if (!visit[next_node] && value >= k) {
                    visit[next_node] = true;
                    total++;
                    Q.add(next_node);
                }
            }
        }
        return total;
    }
}
