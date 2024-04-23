import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class Main {
    // strike count
    public static int cntStrike(int num1, int num2) {
        int n1 = num1 / 100;
        int n2 = num1 % 100 / 10;
        int n3 = num1 % 10;

        int m1 = num2 / 100;
        int m2 = num2 % 100 / 10;
        int m3 = num2 % 10;

        int strike = 0;

        if (n1 == m1) strike++;
        if (n2 == m2) strike++;
        if (n3 == m3) strike++;

        return strike;
    }

    // ball count
    public static int cntBall(int num1, int num2) {
        int n1 = num1 / 100;
        int n2 = num1 % 100 / 10;
        int n3 = num1 % 10;

        int m1 = num2 / 100;
        int m2 = num2 % 100 / 10;
        int m3 = num2 % 10;

        int ball = 0;

        if (n1 != m1 && (n1 == m2 || n1 == m3)) ball++;
        if (n2 != m2 && (n2 == m1 || n2 == m3)) ball++;
        if (n3 != m3 && (n3 == m1 || n3 == m2)) ball++;

        return ball;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        ArrayList<Integer> cases = new ArrayList<>();

        // cases에 모든 경우의 수 추가
        for (int i = 123; i <= 987; i++) {
            int n1 = i / 100;
            int n2 = i % 100 / 10;
            int n3 = i % 10;
            
            if (n2 == 0 || n3 == 0) {
                continue;
            }

            if (n1 == n2 || n1 == n3 || n2 == n3 ) {
                continue; // 중복되는 숫자를 제외
            }

            cases.add(i); // 가능한 모든 세 자리 숫자
        }

        for (int index = 0; index < n; index++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int input = Integer.parseInt(st.nextToken());
            int strike = Integer.parseInt(st.nextToken());
            int ball = Integer.parseInt(st.nextToken());

            // 모든 경우의 수에서 input이 strike, ball이 가능한 모든 조건을 필터링

            // case 1: 반복문에서 조건에 안 맞는 경우 remove
            /* 
            for (int c = cases.size() - 1; c >= 0; c--) {
                int num = cases.get(c);

                int tStrike = cntStrike(input, num);
                int tBall = cntBall(input, num);

                if (tStrike != strike || tBall != ball) {
                    cases.remove(new Integer(num));
                }
            }
            */            

            // case 2: removeIf를 사용한 방법, 더 좋은 방법이 없을까 찾던 중 GPT가 알려줌
            cases.removeIf(num -> {
                int tStrike = cntStrike(input, num);
                int tBall = cntBall(input, num);

                return tStrike != strike || tBall != ball; // 조건에 맞지 않는 경우 삭제
            });
        }

        System.out.println(cases.size());
    }
}