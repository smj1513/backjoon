package ssafyclass.combination;

public class Main {
    static int[] arr;//원본 배열
    static int r;//몇개를뽑을까?
    static int[] output = new int[r]; //뽑은 조합을 저장할 배열

    public static void main(String[] args) {

    }

    public static void combination(int start, int depth) {
        //base case : r개의 원소를 모두 뽑았을 경우
        if (depth == r) {
            //뭔가 수행할 작업
            return;
        } else {
            for (int i = start; i < arr.length; i++) {
                output[depth] = arr[i]; // 현재 경우의 수에 원소 추가
                //다음 원소는 현재 뽑은 원소의 다음 인덱스 부터 뽑도록 호출
                combination(i + 1, depth + 1);
            }
        }
    }
}
