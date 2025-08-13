package ssafyclass.powerset;

import java.util.Scanner;

// 부분 집합
public class Main {
    static int[] input; // 숫자 배열
    static boolean[] isSelected; // 부분 집합에 포함/비포함 여부를 저장한 배열
    static int N;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        input = new int[N];
        isSelected = new boolean[N];

    }

    public static void generateSubSet(int depth) {
        if (depth == N) { //마지막 원소를 고려했다면?
            for (int i = 0; i < input.length; i++) {
                System.out.println(isSelected[i] ? input[i] : "X");
            }
            System.out.println();
            return;
        } else {
            isSelected[depth] = true; // 해당 자리에 원소를 넣기
            generateSubSet(depth + 1); // 자리를 내려가면서 마치 트리 구조로
            isSelected[depth] = false; // 해당 자리에 원소를 넣지 않기
            generateSubSet(depth + 1); //
        }
    }
}