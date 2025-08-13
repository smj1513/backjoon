package BOJ15650;

import java.util.Scanner;

public class Main {
    static int N, R;
    static int[] numbers;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        R = sc.nextInt();
        numbers = new int[N];
        combination(0, 0);

    }

    public static void combination(int start, int depth) {
        if (depth == N) {
            System.out.print(numbers[depth] + " ");
            return;
        }
        for (int i = start; i < R; i++) {
            numbers[start] = i;
            combination(i + 1, depth + 1);
        }

    }
}
