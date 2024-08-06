package Java;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class J3187 {
    static int R,C,total_Sheep = 0, wolves = 0;
    static boolean[][] visit;
    static char[][] fence;
    

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        R = sc.nextInt();
        C = sc.nextInt();
        sc.nextLine();
        fence = new char[R][];
        visit = new boolean[R][C];

        for(int i=0; i<R; i++) {
            fence[i] = sc.nextLine().toCharArray();
        }

        for(int i=0; i<R; i++) {
            for(int j=0; j<C; j++) {
                if (!visit[i][j]) {
                    search(i, j);
                }
            }
        }
        System.out.println(total_Sheep + " " + wolves);
    }

    static void search(int i, int j) {
        Deque<int[]> Q = new ArrayDeque<>();
        Q.add(new int[]{i, j});
        int sheep = 0;
        int wolf = 0;

        if (fence[i][j] == 'v')
            wolf++;
        if (fence[i][j] == 'k')
            sheep++;
        visit[i][j] = true;

        while (!Q.isEmpty()) {
            int[] pos = Q.pop();
            int x = pos[1];
            int y = pos[0];

            for(int k=0; k<4; k++) {
                int[] dx = {1,-1,0,0};
                int[] dy = {0,0,1,-1};
                int X = x+dx[k];
                int Y = y+dy[k];
                
                if (0 <= X && X < C && 0 <= Y && Y < R) {
                    if (!visit[Y][X] && fence[Y][X] != '#') {
                        visit[Y][X] = true;
                        if (fence[Y][X] == 'v') wolf ++;
                        if (fence[Y][X] == 'k') sheep ++;
                        Q.add(new int[]{Y,X});
                    }
                }
            }
        }

        if (sheep > wolf) {
            total_Sheep += sheep;
        } else {
            wolves += wolf;
        }
    }
}
