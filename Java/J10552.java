package Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class J10552 {
    static ArrayList<ArrayList<Integer>> array;
    static boolean[] visit;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NMP = br.readLine().split(" ");
        int N = Integer.parseInt(NMP[0]);
        int M = Integer.parseInt(NMP[1]);
        int P = Integer.parseInt(NMP[2]);
        visit = new boolean[M+1];
        array = new ArrayList<>();
        
        for(int i=0; i<M+1; i++) {
            array.add(new ArrayList<>());
        }

        for(int i=0; i<N; i++) {
            String[] AB = br.readLine().split(" ");
            int A = Integer.parseInt(AB[0]);
            int B = Integer.parseInt(AB[1]);
            if (array.get(B).isEmpty()) {
                array.get(B).add(A);
            }
        }
        dfs(P, 0);
    }

    static void dfs(int node, int count) {
        if (visit[node]) {
            System.out.println(-1);
            System.exit(0);
        } 
        else if (array.get(node).isEmpty()) {
            System.out.println(count);
            System.exit(0);
        }
        visit[node] = true;
        dfs(array.get(node).get(0), count+1);
    }
}
