package SWEA1486;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
    static int[] height;
    static int min = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int N = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            height = new int[N];
            int S = 0;
            st = new StringTokenizer(br.readLine(), " ");
            for (int i = 0; i < N; i++) {
                height[i] = Integer.parseInt(st.nextToken());
                S += height[i];
            }
            Arrays.sort(height);
            S -= B;
            for (int i = 0; i < N; i++) {

                S -= height[i];
                min = Math.min(min, S - B);
            }
            System.out.println("#" + tc + " " + min);
            min = Integer.MAX_VALUE;
        }
    }
}
