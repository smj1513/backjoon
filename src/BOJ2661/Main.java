package BOJ2661;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int[] arr = {1, 2, 3};
    static boolean[] visited;
    static int[] temp;
    static int N;
    static int[] result;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        temp = new int[N];
        visited = new boolean[N];
        backTracking(0);
    }

    public static void backTracking(int depth) {
        if (depth == N) {
            System.out.println(Arrays.toString(temp));
        } else {
            for (int i = 0; i < arr.length; i++) {
                if (!visited[depth]) {
                    temp[depth] = arr[i];
                    for (int j = depth; j > 1; j--) {
                        if(temp[j] == temp[j-1]){

                        }
                    }
                    visited[depth] = true;
                    backTracking(depth + 1);
                    visited[depth] = false;
                }
            }
        }
    }
}
