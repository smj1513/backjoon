package BOJ2492;

import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

class Position {
    int x;
    int y;

    public Position(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static List<Position> jewels = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int T = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            jewels.add(new Position(x, y));
        }

        int maxJewels = 0;
        int resultX = 0;
        int resultY = 0;
        for (Position pX : jewels) {
            int left = pX.x;
            int right = left + K;

            List<Position> yCandidates = new ArrayList<>();
            for (Position jewel : jewels) {
                if (jewel.x >= left && jewel.x <= right) {
                    yCandidates.add(jewel);
                }
            }

            yCandidates.sort(Comparator.comparingInt(p -> p.y));

            int currentMaxInStrip = 0;
            int bestYInStrip = 0;
            if (!yCandidates.isEmpty()) {
                int p1 = 0;
                for (int p2 = 0; p2 < yCandidates.size(); p2++) {
                    while (yCandidates.get(p2).y - yCandidates.get(p1).y > K) {
                        p1++;
                    }

                    int count = p2 - p1 + 1;
                    if (count > currentMaxInStrip) {
                        currentMaxInStrip = count;
                        bestYInStrip = yCandidates.get(p1).y;
                    }
                }

            }

            if (currentMaxInStrip > maxJewels) {
                maxJewels = currentMaxInStrip;
                resultX = left;
                resultY = bestYInStrip;
            }
        }
        System.out.println(resultX + " " + resultY);
        System.out.println(maxJewels);
    }
}
