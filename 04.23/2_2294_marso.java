import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] coins = new int[n];
        int[] arr = new int[k+1];

        for (int i = 0; i < n; i++) {
            coins[i] = Integer.parseInt(br.readLine());
        } // 여기까지 입력

        Arrays.sort(coins);
        Arrays.fill(arr, Integer.MAX_VALUE-1);
        arr[0] = 0;

        /*

           1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
        1  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
        5  - - - - 1 1 1 1 1  2  2  2  2  2  3 
        12 - - - - - - - - - -- --  1  1  1  1
        
           1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
        1  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
        5  1 2 3 4 1 2 3 4 5  2  3  4  5  6  3 <-- 기준 arr[6] = arr[6 -5(coin)] + 1 or arr[6] 중애 작은 거
        12 1 2 3 4 1 2 3 4 5  2  3  1  2  3  3

         */

        for (int i = 0; i < n; i++) {
            for (int j = coins[i]; j <= k; j++) { // coins[i] 보다 작은 경우 무시
                arr[j] = Math.min(arr[j - coins[i]] + 1, arr[j]); 
            }
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        if (arr[k] == Integer.MAX_VALUE-1) {
            bw.write("-1");
            bw.flush();   //남아있는 데이터를 모두 출력시킴
            bw.close();   //스트림을 닫음
            return;
        }

        bw.write(arr[k]+"\n");
        bw.flush();   //남아있는 데이터를 모두 출력시킴
        bw.close();   //스트림을 닫음
    }
}