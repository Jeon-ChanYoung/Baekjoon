package Java;

import java.util.Scanner;

public class J11123 {
    static int H,W;
    static char[][] grid;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while(T-->0) {
            H = sc.nextInt();
            W = sc.nextInt();sc.nextLine();
            int count = 0;
            grid = new char[H][];

            for(int i=0; i<H; i++) {
                grid[i] = sc.nextLine().toCharArray();
            }

            for(int y=0; y<H; y++) {
                for(int x=0; x<W; x++) {
                    if (grid[y][x] == '#') {
                        grid[y][x] = '.';
                        count++;
                        dfs(x,y);
                    }
                }
            }
            System.out.println(count);
        }
    }

    static void dfs(int x, int y) {
        int[] dx = {1,-1,0,0};
        int[] dy = {0,0,1,-1};
        for(int i=0; i<4; i++) {
            int X = x+dx[i];
            int Y = y+dy[i];
            if (0<=X && X<W && 0<=Y && Y<H && grid[Y][X] == '#') {
                grid[Y][X] = '.';
                dfs(X,Y);
            }
        }
    }
}
