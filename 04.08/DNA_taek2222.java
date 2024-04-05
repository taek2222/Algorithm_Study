/*
    https://www.acmicpc.net/problem/1969

    첫 줄에 DNA의 수 N과 문자열의 길이 M이 주어진다.
    그리고 둘째 줄부터 N+1번째 줄까지 N개의 DNA가 주어진다.
    N은 1,000보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다.

    - 입력
        5 8
        TATGATAC
        TAAGCTAC
        AAAGATCC
        TGAGATAC
        TAAGATGT

    - 출력
        TAAGATAC
        7
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class DNA_taek2222 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        // DNA 수 N
        int N = Integer.parseInt(st.nextToken());

        // 문자열 길이 M
        int M = Integer.parseInt(st.nextToken());

        // DNA 입력
        String[] array = new String[N];
        for(int i = 0; i < N; i++)
            array[i] = br.readLine();

        // ATGC 값 배열
        int[][] ATGC = new int[4][M];

        // 각 세로 라인의 ATGC 갯수 구하기
        for(int i = 0; i < M; i++) {
            for(int j = 0; j < N; j++) {
                switch(array[j].charAt(i)) {
                    case 'T' : ATGC[0][i]++; break;
                    case 'G' : ATGC[1][i]++; break;
                    case 'C' : ATGC[2][i]++; break;
                    case 'A' : ATGC[3][i]++; break;
                }
            }
        }

        // 정답 배열, 총 Hamming Distance
        String[] answer = new String[M];
        int hamming = 0;

        // 정답 배열 저장
        for (int i = 0; i < M; i++) {
            int max = 0;
            int max_line = 2;
            for(int j = 0; j < 4; j++) {
                if(max <= ATGC[j][i]) {
                    max = ATGC[j][i];
                    max_line = j;
                }
            }

            // 정답 라인 확정
            switch (max_line) {
                case 0 : answer[i] = "T"; hamming += (N - max); break;
                case 1 : answer[i] = "G"; hamming += (N - max); break;
                case 2 : answer[i] = "C"; hamming += (N - max); break;
                case 3 : answer[i] = "A"; hamming += (N - max); break;
            }
        }

        // 정답 출력
        for (String c : answer)
            System.out.print(c);
        System.out.println();
        System.out.print(hamming);
    }
}