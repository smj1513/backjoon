package BOJ5567;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static List<List<Integer>> graph = new ArrayList<>();
    static boolean[] visited;
    static int cnt = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        visited = new boolean[n+1];
        int m = Integer.parseInt(br.readLine());
        for(int i = 0; i <= m ; i++){
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        dfs(1);
        System.out.println(cnt);
    }

    public static void dfs(int n){
        visited[n] = true;
        for (int v : graph.get(n)){
            if(!visited[v]){
                cnt++;
                dfs(v);
            }
        }
    }
}
