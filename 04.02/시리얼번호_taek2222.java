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
public class 시리얼번호_taek2222{
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        // 시리얼 배열 생성
        int N = Integer.parseInt(bufferedReader.readLine());
        String[] array = new String[N];

        // 시리얼 번호 입력
        for (int i = 0; i < N; i++)
            array[i] = bufferedReader.readLine();

        Arrays.sort(array, (o1, o2) -> {
            if (o1.length() < o2.length())
                return -1;
            else if(o1.length() == o2.length())
                if(num_add(o1) == num_add(o2))
                    return o1.compareTo(o2);
                else
                    return Integer.compare(num_add(o1), num_add(o2));
            else return 1;
        });

        for(String s : array)
            System.out.println(s);
    }

    public static int num_add(String s) {
        int sum = 0;
        for (int i = 0; i < s.length(); i++) {
            if(s.charAt(i)>='0'&&s.charAt(i)<='9')
                sum += s.charAt(i)-'0';
        }
        return sum;
    }
}