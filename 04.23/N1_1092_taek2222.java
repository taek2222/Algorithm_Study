/*
    https://www.acmicpc.net/problem/1092

    지민이는 항구에서 일한다.
    그리고 화물을 배에 실어야 한다.
    모든 화물은 박스에 안에 넣어져 있다.
    항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다.
    모든 크레인은 동시에 움직인다.

    각 크레인은 무게 제한이 있다.
    이 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다.
    모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성하시오.

    - 입력
        첫째 줄에 N이 주어진다.
        N은 50보다 작거나 같은 자연수이다.
        둘째 줄에는 각 크레인의 무게 제한이 주어진다.
        이 값은 1,000,000보다 작거나 같다. 셋째 줄에는 박스의 수 M이 주어진다.
        M은 10,000보다 작거나 같은 자연수이다.
        넷째 줄에는 각 박스의 무게가 주어진다.
        이 값도 1,000,000보다 작거나 같은 자연수이다.

    - 출력
        첫째 줄에 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 출력한다.
        만약 모든 박스를 배로 옮길 수 없으면 -1을 출력한다.

    - 예제 입력
        3
        6 8 9
        5
        2 5 2 4 7
    - 예제 출력
        2
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class N1_1092_taek2222 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 크레인 입력
        int N = Integer.parseInt(br.readLine());
        Integer[] crane = new Integer[N];
        st = new StringTokenizer(br.readLine());

        for(int i = 0; i < N; i++)
            crane[i] = Integer.parseInt(st.nextToken());

        // 박스 입력
        int M = Integer.parseInt(br.readLine());
        ArrayList<Integer> box= new ArrayList<>();
        st = new StringTokenizer(br.readLine());

        for(int i = 0; i < M; i++)
            box.add(Integer.parseInt(st.nextToken()));

        Arrays.sort(crane, Comparator.reverseOrder());
        box.sort(Collections.reverseOrder());

        // 비정상 시 종료
        if(box.get(0) > crane[0]) {
            System.out.println(-1);
            System.exit(0);
        }


        int cycle = 0;
        while(!(box.isEmpty())) {
            int box_position = 0;

            for(int i = 0; i < N;) {
                // 크레인 적재
                if(box.get(box_position) <= crane[i]) {
                    box.remove(box_position);
                    i++;
                }
                else
                    box_position++;

                if(box.size() == box_position)
                    break;
            }

            cycle++;
        }

        System.out.print(cycle);
    }
}
