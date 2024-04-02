import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/*
    https://www.acmicpc.net/problem/1431

    첫째 줄에 기타의 개수 N이 주어진다.
    N은 50보다 작거나 같다.
    둘째 줄부터 N개의 줄에 시리얼 번호가 하나씩 주어진다.
    시리얼 번호의 길이는 최대 50이고, 알파벳 대문자 또는 숫자로만 이루어져 있다.
    시리얼 번호는 중복되지 않는다.

    - 입력
        5
        ABCD
        145C
        A
        A910
        Z321

    - 출력
        A
        ABCD
        Z321
        145C
        A910
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(bufferedReader.readLine());

        String[] array = new String[N];

        // 시리얼 번호
        for(int i = 0; i < N; i++)
            array[i] = bufferedReader.readLine();

        for(int i = 0; i < N-1; i++) {
            int num;
            num = lenComparison(array[i], array[i+1]);
            numComparison(array[i], array[i+1]);
            System.out.println(array[i] + ": 비교 :" + array[i+1] + " = " + num);
        }

    }

    // 1. 문자열 길이 비교 (v1이 크다 : 양수 | 같다 : 0 | v2가 크다 : 음수 )
    static int lenComparison(String v1, String v2) {
        return Integer.compare(v1.length(), v2.length());
    }

    // 2. 문자열의 숫자 비교 (v1이 크다 : 양수 | 같다 : 0 | v2가 크다 : 음수 )
    static int numComparison(String v1, String v2) {
        int v1_total = 0;
        int v2_total = 0;

        for(int i = 0; i < v1.length(); i++) {
            char ch_1 = v1.charAt(i);
            char ch_2 = v2.charAt(i);

            if (48 <= ch_1 && ch_1 <= 57)
                v1_total += ch_1 - 48;

            if (48 <= ch_2 && ch_2 <= 57)
                v2_total += ch_2 - 48;
        }

        return v1_total - v2_total;
    }

    // 3. 문자열 하나씩 비교 사전 순 정렬 (v1이 크다 : 양수 | v2가 크다 : 음수 )
    static int englishSort(String v1, String v2) {
        for(int i = 0; i < v1.length(); i++) {
            char ch_1 = v1.charAt(i);
            char ch_2 = v2.charAt(i);

            if(ch_1 == ch_2)
                continue;

            if(ch_1 > ch_2)
                return 1;
            else
                return -1;
        }
    }
}