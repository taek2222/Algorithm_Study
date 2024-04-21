import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        char[][] arr = new char[n][];

        for (int i = 0; i < n; i++) {
            arr[i] = br.readLine().toCharArray();
        }

        // 알고리즘이 생각이 안 나..!!!!!!
    }
}