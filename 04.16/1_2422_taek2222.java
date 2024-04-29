import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/*
    https://www.acmicpc.net/problem/2422

    첫째 줄에 정수 N과 M이 주어진다.
    N은 아이스크림 종류의 수이고,
    M은 섞어먹으면 안 되는 조합의 개수이다.
    아래 M개의 줄에는 섞어먹으면 안 되는 조합의 번호가 주어진다.
    같은 조합은 두 번 이상 나오지 않는다.
    (1 ≤ N ≤ 200, 0 ≤ M ≤ 10,000)

    - 입력
        5 3
        1 2
        3 4
        1 3
    - 결과
        3
*/

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 최종 갯수 반환
        int result = 0;

        // NM 입력 받기
        String[] NM = br.readLine().split(" ");
        int n = Integer.parseInt(NM[0]);
        int m = Integer.parseInt(NM[1]);

        // 판독 가능한 배열 생성
        boolean[][] dirty = new boolean[n+1][n+1];

        for(int i=0; i<m; i++){
            String[] number = br.readLine().split(" ");
            int a = Integer.parseInt(number[0]);
            int b = Integer.parseInt(number[1]);

            dirty[a][b] = true;
            dirty[b][a] = true;
        }

        // 3번의 반복을 진행하지만, 무작위 2개를 고른 수에서 2개를 검사 후 진행.
        // 이후 무작위 번호도 새로 검사를 진행.
        for (int i = 1; i <= n; i++) {
            for(int j=i+1; j<=n; j++){
                if(dirty[i][j]) continue;
                for (int k = j + 1; k <= n; k++) {
                    if(!dirty[j][k] && !dirty[k][i]){
                        result++;
                    }
                }
            }
        }
        System.out.println(result);
    }
}