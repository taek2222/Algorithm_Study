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

        String[] dna = new String[n]; 

        for (int i = 0; i < n; i++) {
            dna[i] = br.readLine();
        }

        /*
         * 
         * String 대신
         * 
         * char[][] dan = new char[n][];
         * 
         * for (int i = 0; i < n; i++) {
         *     dna[] = br.readLine().toCharArray();
         * }
         * 
         */

        char[] answer = new char[m];
        int sum = 0;

        String nucleotide = "ACGT"; // A = 0, C = 1, G = 2, T = 3, new int[26] 대신

        for (int i = 0; i < m; i++) {
            int[] cnt = new int[4];
            int max = 0;
            int maxIndex = 0;

            for (int j = 0; j < n; j++) {
                cnt[nucleotide.indexOf(dna[j].charAt(i))]++;
            }

            for (int j = 0; j < 4; j++) {
                if (cnt[j] > max) {
                    max = cnt[j];
                    maxIndex = j;
                }
            }

            sum += (n - max);
            answer[i] = nucleotide.charAt(maxIndex);
        }

        System.out.println(new String(answer));
        System.out.println(sum);
    }
}