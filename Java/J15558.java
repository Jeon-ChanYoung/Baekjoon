package Java;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class J15558 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();sc.nextLine();
        int[] dx = {1,-1,K};
        int[] dy = {0,0,-1};
        char[][] line = new char[2][];
        boolean[][] visit = new boolean[2][N];
        line[0] = sc.nextLine().toCharArray();
        line[1] = sc.nextLine().toCharArray();
   
        Deque<int[]> Q = new ArrayDeque<>();
        Q.add(new int[]{0,0,0});

        while (!Q.isEmpty()) {
            int[] info = Q.pop();
            int x = info[0];
            int y = info[1];
            int danger = info[2];

            for(int i=0; i<3; i++) {
                int X = x+dx[i];
                int Y = Math.abs(y+dy[i]);

                if (X >= N) {
                    System.out.println(1);
                    System.exit(0);
                }

                if (X > danger && !visit[Y][X] && line[Y][X] == '1') {
                    visit[Y][X] = true;
                    Q.add(new int[]{X,Y,danger+1});
                }
            }
        }
        System.out.println(0);
    }
}
