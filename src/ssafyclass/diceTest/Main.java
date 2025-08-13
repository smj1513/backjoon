package ssafyclass.diceTest;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    //주사위 던지기 1, 2, 3, 4
    static int N;//주사위 몇번 던졌는지?
    static int[] numbers;// 순열 저장할 배열
    static int totalCnt;
    static boolean[] isSelected;

    public static void main(String[] args) {
        //입력으로 주사위 던진 횟수와 던지기 모드 받기
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt(); //던진 횟수
        int M = sc.nextInt(); //던지기 모드
        numbers = new int[N]; //뽑았을 때 주사위를 저장할 배열
//        switch (M) {
//            case 1 -> { //중복 순열
//                dice1(0);
//            }
//            case 2 -> { //그냥 순열
//                isSelected = new boolean[7]; // 중복체크 배열, 주사위 눈이 1~6
//                // 해당 자리에 가능한 주사위 눈을 모두 시도 : 유도 파트
//                dice2(0);
//            }
//            default -> {
//            }
//        }
        System.out.println("총 경우의 수 :" + totalCnt);
    }

    public static void dice1(int depth) {
        if (depth == N) {
            totalCnt++;
            System.out.println(Arrays.toString(numbers));
            return;
        }
        for (int i = 1; i <= 6; i++) {
            numbers[depth] = i;
            dice1(depth + 1);
        }
    }

    public static void dice2(int depth) { // depth : 기존까지 던진 주사위 횟수
        //기저파트
        if (depth == N) { // 다 던졌다면....
            totalCnt++;
            System.out.println(Arrays.toString(numbers));
            return;
        }
        for (int i = 1; i <= 6; i++) {
            if (!isSelected[i]) {
                isSelected[i] = true;
                numbers[depth] = i;
                dice2(depth + 1); //다음 주사위 던지러 가기.
                isSelected[i] = false;
            }
        }
    }
}
