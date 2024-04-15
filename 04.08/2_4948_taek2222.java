import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

/*
    https://www.acmicpc.net/problem/4948

    입력은 여러 개의 테스트 케이스로 이루어져 있다.
    각 케이스는 n을 포함하는 한 줄로 이루어져 있다.
    입력의 마지막에는 0이 주어진다.

    - 입력
        1
        10
        13
        100
        1000
        10000
        100000
        0

    - 출력
        1
        4
        3
        21
        135
        1033
        8392

*/

public class 베르트랑공준_taek2222 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 인수 배열
        ArrayList<Integer> array = new ArrayList<>();

        // 첫 번째 인수
        int num = Integer.parseInt(br.readLine());

        // 최대값
        int max = 0;

        // 최대값 찾기 및 배열 삽입
        while(!(num == 0)) {
            if(num > max)
                max = num;
            array.add(num);
            num = Integer.parseInt(br.readLine());
        }

        // 소수 배열 정의
        boolean[] prime = new boolean[(max*2)+1];

        // 0, 1은 소수가 아니므로 정의
        prime[0] = prime[1] = true;

        // 2부터 에라토스테네스의 체 방식으로 소수 판별
        for(int i = 2; i*i <= prime.length - 1; i++) {
            if(!prime[i]) {
                for (int j = i * i; j <= prime.length - 1; j += i) prime[j] = true;
            }
        }

        // array 저장 했던 인수들을 차례대로 탐색
        for(int i : array) {
            int total = 0;
            for(int j = i+1; j <= i*2; j++)
                if(!prime[j])
                    total++;
            System.out.println(total);
        }
    }
}
