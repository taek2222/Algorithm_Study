import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());   
        int m = Integer.parseInt(st.nextToken());
        
        boolean[][] worst = new boolean[n][n];
        
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            
            int j = Integer.parseInt(st.nextToken()) - 1;
            int k = Integer.parseInt(st.nextToken()) - 1;
            
            worst[j][k] = true;
            worst[k][j] = true;
        } // 여기까지 입력

        int cnt = 0;

        for(int i = 0; i < n-2; i++) {
            for(int j = i+1; j < n; j++) {
                if (worst[i][j]) {
                    continue;
                }

                for (int k = j+1; k < n; k++) {
                    if (worst[j][k] || worst[i][k]) {
                        continue;
                    }
                    
                    cnt++;
                }
            }
        }
        
        System.out.println(cnt);
    }
}