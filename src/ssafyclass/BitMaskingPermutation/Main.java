package ssafyclass.BitMaskingPermutation;

public class Main {
    static int N = 11;
    static int[] origin = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11};
    static int[] number = new int[N];

    public static void main(String[] args) {
        long start = System.nanoTime();
        bitPermutation(0, 0);
        long end = System.nanoTime();
        System.out.println((end-start)/1_000_000_000.0);

    }

    public static void bitPermutation(int depth, int flag) { //flag가 isSelected 배열
        if (depth == N) {
            //System.out.println(Arrays.toString(number));
            return;
        } else {
            for (int i = 0; i < origin.length; i++) {
                if ((flag & (1 << i)) == 0) { //현재 플래그가 사용중이 아니라면
                    number[depth] = origin[i];
                    bitPermutation(depth + 1, flag | 1 << i);
                }
            }
        }
    }
}
