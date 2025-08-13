package SWEA1210;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static int[][] matrix = new int[100][100];
    public static boolean[][] visited = new boolean[100][100];
    public static int[] dx = {0, 0, -1}; //좌 우 상
    public static int[] dy = {-1, 1, 0}; //
    static int startX, startY;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int tc = 1; tc <= 10; ++tc) {
            int a = Integer.parseInt(br.readLine());
            for (int i = 0; i < 100; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine(), " ");
                for (int j = 0; j < 100; j++) {
                    int input = Integer.parseInt(st.nextToken());
                    matrix[i][j] = input;
                    if (input == 2) {
                        startX = i;
                        startY = j;
                    }
                }
            }
            int result = bfs();
            System.out.println("#" + a + " " + result);
            visited = new boolean[100][100];
        }

    }

    public static int bfs() {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{startX, startY});
        int result = 0;
        visited[startX][startY] = true;
        while (!queue.isEmpty()) {
            int[] curPosition = queue.poll();
            int x = curPosition[0];
            int y = curPosition[1];
            for (int i = 0; i < 3; i++) {
                int drx = dx[i] + x;
                int dry = dy[i] + y;
                if (valid(drx, dry) && matrix[drx][dry] == 1 && !visited[drx][dry]) {
                    queue.add(new int[]{drx, dry});
                    visited[drx][dry] = true;
                    if(i == 0 || i == 1)
                        break;
                }
            }
            result = y;
        }
        return result;
    }

    public static boolean valid(int x, int y) {
        return 0 <= x && x < 100 && 0 <= y && y < 100;
    }
}
