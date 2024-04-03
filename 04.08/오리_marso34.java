import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] input = br.readLine().toCharArray();
        String quack = "quack";

        int cnt = 0;

        // while (true) {
        //     int index = 0;

        //     for (int i = 0; i < input.length; i++) {
        //         if (input[i] == -1)
        //             continue;

        //         if (input[i] == quack.charAt(index)) {
        //             input[i] = -1;
        //             index++;
        //         }

        //         if (index == 5) {
        //             cnt++;
        //             break;
        //         }
        //     }

        //     if (index < 5)
        //         break;
        // }

        int[] arr = new int[5]; 

        for (int i = 0; i < input.length; i++) {
            arr[quack.indexOf(input[i])]++;

            if (arr[0] > 0 && arr[1] > 0 && arr[2] > 0 && arr[3] > 0 && arr[4] > 0) {
                cnt++;

                arr[0]--;
                arr[1]--;
                arr[2]--;
                arr[3]--;
                arr[4]--;
            }      
        }

        // 아직 테스트 중

        cnt = cnt == 0 ? -1 : cnt;

        System.out.println(cnt);
    }   
}