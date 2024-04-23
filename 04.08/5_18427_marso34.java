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
        int h = Integer.parseInt(st.nextToken());

        int[][] dp = new int[n+1][h+1];
        String[][] arr = new String[n][];

        for (int i = 1; i <= n; i++) {
            // arr[i-1] = br.readLine().replaceAll(" ", "").toCharArray(); // 공백제거해서 char 배열로, 10 이상이면 문제 있음 
            arr[i-1] = br.readLine().split(" "); 

            if (i == 1) {
                for (String s : arr[0]) {
                    dp[i][Integer.parseInt(s)]++;
                }
            }
            
            dp[i][0] = 1;
        }
        
        for (int i = 2; i <= n; i++) { // 학생
            for (int j = 1; j <= h; j ++) { // 높이
                for (String value : arr[i-1]) {
                    // value 학생 i가 가진 블럭
                    int temp = Integer.parseInt(value);

                    if (j - temp >= 0) {
                        dp[i][j] += dp[i-1][j - temp];
                        dp[i][j] %= 10007;
                    }
                }
                
                dp[i][j] += dp[i-1][j];
                dp[i][j] %= 10007;
            }
        }
        
        System.out.println(dp[n][h]);
    }
}