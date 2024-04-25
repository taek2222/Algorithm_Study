import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/*
    https://www.acmicpc.net/problem/1913

    첫째 줄에 홀수인 자연수 N(3 ≤ N ≤ 999)이 주어진다.
    둘째 줄에는 위치를 찾고자 하는 N2 이하의 자연수가 하나 주어진다.

    - 입력
        7
        35
    - 결과
        49 26 27 28 29 30 31
        48 25 10 11 12 13 32
        47 24 9 2 3 14 33
        46 23 8 1 4 15 34
        45 22 7 6 5 16 35
        44 21 20 19 18 17 36
        43 42 41 40 39 38 37
        5 7
*/

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int target = Integer.parseInt(br.readLine());
        int[][] matrix = new int[N][N];

        // 초기 위치: 매트릭스 중심
        int row = N / 2;
        int col = N / 2;
        int steps = 1; // 한 방향으로 이동할 횟수
        int num = 1; // 채워넣을 숫자

        int targetRow = 0;
        int targetCol = 0;

        while (num <= N * N) {
            // Up
            for (int i = 0; i < steps; i++) {
                matrix[row][col] = num;
                if (num == target) {
                    targetRow = row + 1;
                    targetCol = col + 1;
                }
                if (num++ == N * N) break;
                row--;
            }
            if (num > N * N) break;

            // Right
            for (int i = 0; i < steps; i++) {
                matrix[row][col] = num;
                if (num == target) {
                    targetRow = row + 1;
                    targetCol = col + 1;
                }
                if (num++ == N * N) break;
                col++;
            }
            if (num > N * N) break;

            steps++; // 증가한 스텝 수

            // Down
            for (int i = 0; i < steps; i++) {
                matrix[row][col] = num;
                if (num == target) {
                    targetRow = row + 1;
                    targetCol = col + 1;
                }
                if (num++ == N * N) break;
                row++;
            }

            // Left
            for (int i = 0; i < steps; i++) {
                matrix[row][col] = num;
                if (num == target) {
                    targetRow = row + 1;
                    targetCol = col + 1;
                }
                if (num++ == N * N) break;
                col--;
            }

            steps++; // 다음 레벨을 위해 스텝 증가
        }

        // 매트릭스와 목표 위치 출력
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                sb.append(matrix[i][j]).append(" ");
            }
            sb.append("\n");
        }
        sb.append(targetRow).append(" ").append(targetCol);
        System.out.println(sb);
    }
}