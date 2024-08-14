package Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class J14248 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] Input = br.readLine().split(" ");
        int[] array = new int[N];
        boolean[] visit = new boolean[N];
        int[] bias = {1,-1};
        int S = Integer.parseInt(br.readLine());
        int count = 1;
        visit[S-1] = true;
        
        for(int i=0; i<N; i++) {
            array[i] = Integer.parseInt(Input[i]);
        }

        Deque<Integer> Q = new ArrayDeque<>();
        Q.add(S-1);

        while (!Q.isEmpty()) {
            int x = Q.pop();
            for(int b : bias) {
                int X = x + array[x] * b;
                if (0<=X && X<N && !visit[X]) {
                    visit[X] = true;
                    count++;
                    Q.add(X);
                }
            }
        }
        System.out.println(count);
    }
}
