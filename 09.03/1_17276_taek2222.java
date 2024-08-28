import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {

    static String[][] array;
    static String[][] copyArray;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());

            d = d > 0 ? d / 45 : (360 + d) / 45;

            array = new String[n][n];
            for (int j = 0; j < n; j++) {
                String[] input = br.readLine().split(" ");
                array[j] = input;
            }

            rotation(n, d);

            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    sb.append(array[j][k]);
                    if (k < n-1)
                        sb.append(" ");
                }
                sb.append("\n");
            }
        }

        sb.setLength(sb.length() - 1);

        System.out.println(sb);
    }

    // 45도 d번 돌리는 메서드
    private static void rotation(int n, int d) {

        for (int i = 0; i < d; i++) {
            copyArray = new String[n][n];
            for (int k = 0; k < n; k++)
                copyArray[k] = array[k].clone();

            for (int j = 0; j < n; j++) {
                copyArray[j][n/2] = array[j][j];
                copyArray[j][n-j-1] = array[j][n/2];
                copyArray[n/2][n-j-1] = array[j][n-j-1];
                copyArray[n-j-1][n-j-1] = array[n/2][n-j-1];
            }
            array = copyArray.clone();
        }
    }
}