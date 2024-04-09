import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

/*
    https://www.acmicpc.net/problem/18427

    첫째 줄에 자연수 N, M, H가 공백을 기준으로 구분되어 주어진다.
    (1 ≤ N ≤ 50, 1 ≤ M ≤ 10, 1 ≤ H ≤ 1,000)
    둘째 줄부터 N개의 줄에 걸쳐서 각 학생이 가진 블록들의 높이가 공백을 기준으로 구분되어 주어진다.
    단, 모든 블록의 높이는 1,000 이하의 자연수이며 한 명의 학생이 가지고 있는 모든 블록들의 높이는 서로 다르게 주어진다.

    - 입력
        3 3 5
        2 3 5
        3 5
        1 2 3
    - 출력
        6

*/
public class 함께블록쌓기_taek2222 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        // 초기값 N, M, H 설정
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken()); // 사용 안함
        int H = Integer.parseInt(st.nextToken());

        // 동적 배열 DP 생성 및 사람들 블록 받을 ArrayList 배열 생성
        int[][] DP = new int[N+1][H+1];
        ArrayList<Integer>[] N_block = new ArrayList[N+1];

        // 사용자 블록 삽입
        for(int i = 1; i < N; i++) {
            N_block[i] = new ArrayList<>();
            st = new StringTokenizer(br.readLine());
            while(st.hasMoreTokens())
                N_block[i].add(Integer.parseInt(st.nextToken()));
        }

        // N번째 사람의 높이 0은 항상 1
        for(int i = 0; i <= N; i++)
            DP[i][0] = 1;

        for(int i = 1; i <= N; i++) {

        }
    }

}
