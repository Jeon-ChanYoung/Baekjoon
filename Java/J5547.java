package Java;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class J5547 {
    static Scanner sc = new Scanner(System.in);
    static int W = sc.nextInt();
    static int H = sc.nextInt();

    public static void main(String[] args) {
        sc.nextLine();
        int length = 0;
        int[] dx = { 1, -1, 0, 0 };
        int[] dy = { 0, 0, 1, -1 };
        String[][] array = new String[H + 2][W + 2];
        boolean[][] visit = new boolean[H + 2][W + 2];
        visit[0][0] = true;

        for (int y = 0; y < H + 2; y++) {
            for (int x = 0; x < W + 2; x++) {
                array[y][x] = "0";
            }
        }

        for (int y = 1; y <= H; y++) {
            String[] temp = sc.nextLine().split(" ");
            for (int x = 1; x <= W; x++) {
                array[y][x] = temp[x - 1];
            }
        }

        Deque<int[]> Q = new ArrayDeque<>();
        Q.add(new int[] { 0, 0 });

        while (!Q.isEmpty()) {
            int[] info = Q.pop();
            int x = info[0];
            int y = info[1];

            for (int i = 0; i < 4; i++) {
                int X = x + dx[i];
                int Y = y + dy[i];
                if (isValid(X, Y)) {
                    if (array[Y][X].equals("1")) {
                        length++;
                    } else if (!visit[Y][X]) {
                        visit[Y][X] = true;
                        Q.add(new int[] { X, Y });
                    }
                }
            }
            for (int dyy : new int[] { -1, 1 }) {
                int X = x + new int[] { -1, 1 }[y % 2];
                int Y = y + dyy;
                if (isValid(X, Y)) {
                    if (array[Y][X].equals("1")) {
                        length++;
                    } else if (!visit[Y][X]) {
                        visit[Y][X] = true;
                        Q.add(new int[] { X, Y });
                    }
                }
            }
        }
        System.out.println(length);
    }

    static boolean isValid(int x, int y) {
        return 0 <= x && x <= W+1 && 0 <= y && y <= H+1;
    }
}