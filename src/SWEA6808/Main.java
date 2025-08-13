package SWEA6808;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.Stream;

public class Main {
    static int result1 = 0, result2 = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            int[] kyuCards = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int i = 1;
            int[] numbers = new int[2];
            boolean[] visited = new boolean[kyuCards.length];
            permutation(kyuCards, numbers, visited, 0);
            System.out.printf("#%d %d %d\n", tc, result1, result2);
            result1 = 0;
            result2 = 0;

        }
    }

    public static void permutation(int[] origin, int[] numbers, boolean[] visited, int depth) {
        if (depth == numbers.length) { //2 장을 뽑았다면
            if (numbers[0] > numbers[1]) {
                result1 += numbers[0] + numbers[1];
            } else {
                result2 += numbers[0] + numbers[1];
            }
            return;
        } else {
            for (int i = 0; i < origin.length; i++) {
                if (!visited[i]) {
                    visited[i] = true;
                    numbers[depth] = origin[i];
                    permutation(origin, numbers, visited, depth + 1);
                    visited[i] = false;
                }
            }
        }
    }
}
