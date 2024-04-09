import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = -1;

        while((n = Integer.parseInt(br.readLine())) != 0) {
            boolean[] isPrime = new boolean[2*n+1];
            Arrays.fill(isPrime, true);

            // 에라토스테네스의 체, O(n log log n) 
            for (int i = 2; i*i <= (n * 2); i++) {
                if (isPrime[i]) {
                    for (int j = i*i; j <= (n * 2); j += i) {
                        isPrime[j] = false;
                    }
                }
            }
            
            int cnt = 0;

            for (int i = n+1; i <= 2 * n; i++) {
                if (isPrime[i]) {
                    cnt++;
                }
            }

            System.out.println(cnt);
        }
    }
}