package Java;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class J13565 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt();
        int N = sc.nextInt();
        sc.nextLine();
        int[] dx = {1,-1,0,0};
        int[] dy = {0,0,1,-1};
        char[][] grid = new char[M][];

        for(int i=0; i<M; i++) {
            grid[i] = sc.nextLine().toCharArray();
        }

        Deque<int[]> Q = new ArrayDeque<>();
        for(int i=0; i<N; i++) {
            if (grid[0][i] == '0') {
                Q.add(new int[]{i, 0});
            }
        }

        while (!Q.isEmpty()) {
            int[] pos = Q.pop();
            int x = pos[0];
            int y = pos[1];
            if (y == M-1) {
                System.out.println("YES");
                System.exit(0);
            } 

            for(int i=0; i<4; i++) {
                int X = x+dx[i];
                int Y = y+dy[i];
                if (0<=X && X<N && 0<=Y && Y<M && grid[Y][X] == '0') {
                    grid[Y][X] = '1';
                    Q.add(new int[]{X,Y});
                }
            }
        }
        System.out.println("NO");
    }
}
