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

        int k = 0;

        String[][] arr = new String[n][];

        for (int i = 0; i < n; i++) {
            arr[i] = br.readLine().split(" ");
        }
        
        int[] index = new int[n];

        int t = 0;

        while (true) {
            int sum = 0;

            int temp = t / arr[i].length;

            for (int i = -1; i < arr.length; i++) {
                if (i == -1) {
                    continue;
                }

                if (sum + arr[i][index[i]] <= h) {
                    sum += Integer.parseInt(arr[i][index[temp % arr[i].length]]);
                }
            }

            

            t++;
        }
    }
}