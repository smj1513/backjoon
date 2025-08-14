package BOJ2630;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.stream.Stream;

public class Main {
    static int[][] matrix;
    static int green, white;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        matrix = new int[N][N];
        for (int i = 0; i < N; i++) {
            matrix[i] = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }
        green = white = 0;
        divide(0,0,N);
        System.out.println(white);
        System.out.println(green);
    }

    static void divide(int startX, int startY, int size) {
        int sum = 0;
        for (int i = startX, xEnd = startX + size; i < xEnd; i++) {
            for (int j = startY, yEnd = startY + size; j < yEnd; j++) {
                sum += matrix[i][j];
            }
        }
        if (sum == 0) {
            white++;
        } else if (sum == size * size) {
            green++;
        } else {
            int newSize = size / 2;
            divide(startX, startY, newSize);
            divide(startX + newSize, startY, newSize);
            divide(startX, startY + newSize, newSize);
            divide(startX + newSize, startY + newSize, newSize);
        }
    }
}
