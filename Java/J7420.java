package Java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class J7420 {

    static double distance(int[] p1, int[] p2) {
        return Math.sqrt(Math.pow((p1[0] - p2[0]), 2) + Math.pow((p1[1] - p2[1]), 2));
    }

    static int[][] reversed(int[][] point) {
        int[][] temp = new int[point.length][2];
        for (int i = 0; i < point.length; i++) {
            temp[i] = point[point.length - 1 - i];
        }
        return temp;
    }

    static double CCW(int[] p1, int[] p2, int[] p3) {
        int x1 = p1[0];
        int y1 = p1[1];
        int x2 = p2[0];
        int y2 = p2[1];
        int x3 = p3[0];
        int y3 = p3[1];
        return (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1);
    }

    static int[][] building_convex(int[][] point) {
        ArrayList<int[]> lower = new ArrayList<>();
        ArrayList<int[]> upper = new ArrayList<>();

        for (int[] pos : point) {
            while (lower.size() >= 2 && CCW(lower.get(lower.size() - 2), lower.get(lower.size() - 1), pos) < 0) {
                lower.remove(lower.size() - 1);
            }
            lower.add(pos);
        }
        for (int[] pos : reversed(point)) {
            while (upper.size() >= 2 && CCW(upper.get(upper.size() - 2), upper.get(upper.size() - 1), pos) < 0) {
                upper.remove(upper.size() - 1);
            }
            upper.add(pos);
        }
        lower.remove(lower.size() - 1);
        upper.remove(upper.size() - 1);
        lower.addAll(upper);

        return lower.toArray(new int[lower.size()][]);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int L = sc.nextInt();
        int[][] point = new int[N][2];

        for (int i = 0; i < N; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            int[] pos = { x, y };
            point[i] = pos;
        }

        Arrays.sort(point, (a, b) -> {
            int cmp = Integer.compare(a[0], b[0]);
            if (cmp != 0) {
                return cmp;
            }
            return Integer.compare(a[1], b[1]);
        });

        double total = 0;
        int[][] convex_hull = building_convex(point);

        for (int i = 0; i < convex_hull.length; i++) {
            total += distance(convex_hull[i], convex_hull[(i + 1) % convex_hull.length]);
        }
        total += 2 * L * Math.PI;
        System.out.println(Math.round(total));
        sc.close();
    }
}