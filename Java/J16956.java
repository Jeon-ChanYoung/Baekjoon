package Java;

import java.util.Scanner;

public class J16956 {
    static int R,C;
    static char[][] farm;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        R = sc.nextInt();
        C = sc.nextInt();
        farm = new char[R][];
        sc.nextLine();

        for(int i=0; i<R; i++) {
            char[] array = sc.nextLine().toCharArray();
            farm[i] = array;
        }

        emptyToFence();

        if (check()) {
            System.out.println(1);
            for(char[] array : farm) {
                System.out.println(new String(array));
            }
        } else {
            System.out.println(0);
        }
        
    }

    static void emptyToFence() {
        for(int i=0; i<R; i++) {
            for(int j=0; j<C; j++) {
                if (farm[i][j] == '.') {
                    farm[i][j] = 'D';
                }
            }
        }
    }

    static boolean check() {
        for(int i=0; i<R; i++) {
            for(int j=0; j<C; j++) {
                if (farm[i][j] == 'S') {
                    for(int k=0; k<4; k++) {
                        int[] dx = {1,-1,0,0};
                        int[] dy = {0,0,1,-1};
                        int X = j+dx[k];
                        int Y = i+dy[k];
                        if ((0 <= X && X < C) && (0 <= Y && Y < R) && farm[Y][X] == 'W')
                            return false; 
                    }
                }
            }
        }
        return true;
    }
}
