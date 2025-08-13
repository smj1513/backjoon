package ssafyclass.nextPermutation;

import java.util.Arrays;
import java.util.Scanner;

// N개의 수를 입력 받아 순서적으로 모두 나열하는 순열 생성
public class Main {
    static int[] origin = new int[11];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        for(int i = 1; i <=11; i++){
            origin[i-1] = i;
        }
        //step 0 : 전처리 가장 작은 순열로 정렬
        long start = System.nanoTime();
        Arrays.sort(origin);
        do {//현재 상태(가장 작은 순열)을 먼저 사용하고 그 다음 순열
            //System.out.println(Arrays.toString(origin));
        } while (nextPermutation());
        long end = System.nanoTime();
        System.out.println((end - start) / 1_000_000_000.0);
    }

    public static boolean nextPermutation() {
        //현재 주어진 수들의 배열(number)을 받아서 사전순으로 다음 순열을 생성
        //numbers 배열의 상태가 바뀜.
        //현 배열의 순열 상태에서 사전순 다음 순열 생성 후 다음 순열이 존재한다면 true 아니면 false
        //step 1. 꼭대기(i)를 찾아 바로 앞 교환 위치 찾기 (꼭대기가 i라면 교환위치는 i - 1)
        int i = origin.length - 1;
        while (i > 0 && origin[i - 1] >= origin[i]) { // 나보다 줄어드는 모습이거나
            --i;
        }

        if (i == 0) { // i가 0까지 쭉 오름 차순이다 == 다음순열이 없다
            return false;
        }
        //step 2. 교환 위치에 값을 크게 만들 자신보다 뒤쪽에서 큰 값 중 가장 작은 값 찾기.
        int j = origin.length - 1;
        while (origin[i - 1] >= origin[j]) {
            --j;
        }
        //step 3. i - 1 위치값과 j 위치값 교환
        swap(i - 1, j);

        //step 4. 꼭대기(i)부터 뒤의 모든 순열을 가장 작은 형태로 만듦(오름차순 형태)
        int k = origin.length - 1;
        while (i < k) {
            swap(i++, k--);
        }
        return true;
    }

    private static void swap(int a, int b) {
        int temp = origin[a];
        origin[a] = origin[b];
        origin[b] = temp;
    }
}
