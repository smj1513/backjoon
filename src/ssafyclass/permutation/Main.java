package ssafyclass.permutation;

public class Main {
    static int[] arr; //원본 배열
    static int r; //몇개를 뽑을 건지?
    static int[] output; //현재 순열을 저장하는 배열
    static boolean[] visited; // 해당 자리에 들어갔는지?

    public static void main(String[] args) {

    }

    static void permutation(int depth) {
        if (depth == r) { //뽑을 개수만큼 다 뽑았다면?
            // 작업
            return;
        }
        for (int i = 0; i < arr.length; i++) {
            //아직 사용하지 않은 원소라면
            if (!visited[i]) {
                visited[i] = true; //사용한다고 표시
                output[depth] = arr[i]; //현재 깊이에 원소 추가
                permutation(depth + 1);//다음 원소를 뽑기
                //복사용 배열을 초기화 해야하지만 덮어씌워 지므로 pass
                visited[i] = false; // 재귀호출이 끝나면 다음 경우에 수를 위해 초기화
            }
        }
    }
}
