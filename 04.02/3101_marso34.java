/*
    https://www.acmicpc.net/problem/3101
    
    1부터 N^2까지 수가 지그재그 대각선 순서로 채워진 N*N 행렬

    ex) N=6일 때
    1	2	6	7	15	16
    3	5	8	14	17	26
    4	9	13	18	25	27
    10	12	19	24	28	33
    11	20	23	29	32	34
    21	22	30	31	35	36

    목표: 토끼가 방문한 칸에 있는 수의 합

    - 토끼의 처음 위치 (0, 0)
    - 토끼는 인접한 칸으로 점프할 수 있다. (위, 아래, 오른쪽, 왼쪽)
    - 같은 칸을 여러 번 방문할 경우에도 방문할 때 마다 더해야 한다. 
    - 토끼가 행렬을 벗어나는 경우는 없다.

    입력
    6 8         <-- N, K (1 ≤ N ≤ 100,000, 1 ≤ K ≤ 300,000) N은 행렬의 크기, K는 토끼가 점프한 횟수이다.
    DDRRUULL    <-- 문자열의 길이 K

 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        String direction = br.readLine();

        int currentX = 0;
        int currentY = 0;
        long sum = 1;

        for (int i = 0; i < k; i++) {
            char dir = direction.charAt(i);

            if (dir == 'U') {
                currentX--;
            } else if (dir == 'D') {
                currentX++;
            } else if (dir == 'L') {
                currentY--;
            } else if (dir == 'R') {
                currentY++;
            }

            sum += getValue(n, currentX, currentY);
        }

        System.out.println(sum);
    }

    // 테스트 코드
    private static void printArray(long n) {
        for (long i = 0; i < n; i++) {
            for (long j = 0; j < n; j++) {
                System.out.printf("%2d ", getValue(n, i, j));
            }

            System.out.println();
        }
    }

    private static long getValue(long n, long x, long y) {
        // (0,0) (0,1) (0,2) (0,3) (0,4) (0,5)
        // (1,0) (1,1) (1,2) (1,3) (1,4) (1,5)
        // (2,0) (2,1) (2,2) (2,3) (2,4) (2,5)
        // (3,0) (3,1) (3,2) (3,3) (3,4) (3,5)
        // (4,0) (4,1) (4,2) (4,3) (4,4) (4,5)
        // (5,0) (5,1) (5,2) (5,3) (5,4) (5,5)

        // 대각선 한 라인마다 1씩 증가하는 등차수열
        // n번 라인 후 부터는 1씩 감소하는 등차수열
        // 등차수열의 합 공식을 이용하여 합을 계산, n(2a + (n-1)d) /2

        // line = (x, y)가 속한 라인 전 라인
        long line = x + y;
        long sum = 0L;

        if (line <= n) {
            sum = line * (line + 1) / 2;
        } else { // line이 n보다 커지면 2개의 등차수열
            long temp = n * (n + 1) / 2;
            sum = temp + (line - n) * (3 * n - line - 1) / 2;
        }

        // order = (x, y)가 속한 라인에서 몇 번째인지
        // (x, y)가 속한 라인이 짝수면 좌하향, 홀수면 우상향
        long order = (line + 1) % 2 == 0 ? x + 1 : y + 1;

        if (line + 1 > n) {
            order -= line + 1 - n;
        }

        return sum + order;
    }
}