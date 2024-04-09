import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/*
    https://www.acmicpc.net/problem/12933

    첫째 줄에 영선이가 녹음한 소리가 주어진다.
    소리의 길이는 5보다 크거나 같고,
    2500보다 작거나 같은 자연수이고,
    'q','u','a','c','k'로만 이루어져 있다.

    - 입력
        quqacukqauackck

    - 출력
        2
*/
public class 오리_taek2222 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 오리 소리 배열 하나씩 분할
        String[] quack = br.readLine().split("");

        // 오리 소리 정렬을 위한 배열
        String[] answer = new String[quack.length];

        // 각 소리가 들어갈 위치 선언
        // q_position 값은 0으로 선언해 초기 위치 선언
        int q_position = 0;
        int u_position, a_position, c_position, k_position;
        u_position = a_position = c_position = k_position = -1;

        // 최소 오리 수
        int duck = 0;

        // 소리의 수가 5의 배수가 아니면 거르기
        if(!(quack.length % 5 == 0)) {
            System.out.println(-1);
            System.exit(0);
        }

        for (String s : quack) {
            switch (s) {
                case "q":
                    if (!(duck == 0))
                        duck--;

                    if(q_position >= quack.length) {
                        System.out.println(-1);
                        System.exit(0);
                    }

                    answer[q_position] = s;

                    q_position += 5;

                    if (u_position == -1)
                        u_position = 1;

                    break;

                case "u":
                    if(u_position == -1 || u_position > quack.length || answer[u_position-1] == null) {
                        System.out.println(-1);
                        System.exit(0);
                    }

                    answer[u_position] = s;
                    u_position += 5;

                    if (a_position == -1)
                        a_position = 2;

                    break;

                case "a":
                    if(a_position == -1 || a_position > quack.length || answer[a_position-1] == null) {
                        System.out.println(-1);
                        System.exit(0);
                    }

                    answer[a_position] = s;
                    a_position += 5;

                    if (c_position == -1)
                        c_position = 3;
                    break;

                case "c":
                    if(c_position == -1 || c_position > quack.length || answer[c_position-1] == null) {
                        System.out.println(-1);
                        System.exit(0);
                    }
                    answer[c_position] = s;
                    c_position += 5;

                    if (k_position == -1)
                        k_position = 4;

                    break;

                case "k":
                    duck++;
                    if(k_position == -1 || k_position > quack.length || answer[k_position-1] == null) {
                        System.out.println(-1);
                        System.exit(0);
                    }
                    answer[k_position] = s;
                    k_position += 5;

                    break;
            }
        }
        // 정답
        System.out.println(duck);
    }
}