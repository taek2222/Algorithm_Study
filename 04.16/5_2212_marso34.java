import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        
        int[] answer = new int[n-1];
        
        for (int i = 0; i < n-1; i++) {
            answer[i] = arr[i+1] - arr[i];
        }
        
        Arrays.sort(answer);

        int sum = 0;

        for (int i = 0; i < n - k; i++) {
            sum += answer[i];
        }
        
        System.out.println(sum);
    }
}