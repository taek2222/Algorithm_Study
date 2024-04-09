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

        // 미완성

    }
}