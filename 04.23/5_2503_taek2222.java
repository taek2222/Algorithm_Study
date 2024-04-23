import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
    https://www.acmicpc.net/problem/2503

    정보문화진흥원 정보 영재 동아리에서 동아리 활동을 하던 영수와 민혁이는 쉬는 시간을 틈타 숫자야구 게임을 하기로 했다.

    영수는 1에서 9까지의 서로 다른 숫자 세 개로 구성된 세 자리 수를 마음속으로 생각한다. (예: 324)
    민혁이는 1에서 9까지의 서로 다른 숫자 세 개로 구성된 세 자리 수를 영수에게 묻는다. (예: 123)
    민혁이가 말한 세 자리 수에 있는 숫자들 중 하나가 영수의 세 자리 수의 동일한 자리에 위치하면 스트라이크 한 번으로 센다. 숫자가 영수의 세 자리 수에 있긴 하나 다른 자리에 위치하면 볼 한 번으로 센다.
    예) 영수가 324를 갖고 있으면

    429는 1 스트라이크 1 볼이다.
    241은 0 스트라이크 2 볼이다.
    924는 2 스트라이크 0 볼이다.
    영수는 민혁이가 말한 수가 몇 스트라이크 몇 볼인지를 답해준다.
    민혁이가 영수의 세 자리 수를 정확하게 맞추어 3 스트라이크가 되면 게임이 끝난다. 아니라면 민혁이는 새로운 수를 생각해 다시 영수에게 묻는다.
    현재 민혁이와 영수는 게임을 하고 있는 도중에 있다. 민혁이가 영수에게 어떤 수들을 물어보았는지, 그리고 각각의 물음에 영수가 어떤 대답을 했는지가 입력으로 주어진다. 이 입력을 바탕으로 여러분은 영수가 생각하고 있을 가능성이 있는 수가 총 몇 개인지를 알아맞혀야 한다.

    아래와 같은 경우를 생각해보자.

    민혁: 123
    영수: 1 스트라이크 1 볼.
    민혁: 356
    영수: 1 스트라이크 0 볼.
    민혁: 327
    영수: 2 스트라이크 0 볼.
    민혁: 489
    영수: 0 스트라이크 1 볼.
    이때 가능한 답은 324와 328, 이렇게 두 가지이다.

    영수는 동아리의 규율을 잘 따르는 착한 아이라 민혁이의 물음에 곧이곧대로 정직하게 답한다. 그러므로 영수의 답들에는 모순이 없다.

    민혁이의 물음들과 각각의 물음에 대한 영수의 답이 입력으로 주어질 때 영수가 생각하고 있을 가능성이 있는 답의 총 개수를 출력하는 프로그램을 작성하시오.

    - 입력
        첫째 줄에는 민혁이가 영수에게 몇 번이나 질문을 했는지를 나타내는 1 이상 100 이하의 자연수 N이 주어진다.
        이어지는 N개의 줄에는 각 줄마다 민혁이가 질문한 세 자리 수와 영수가 답한 스트라이크 개수를 나타내는 정수와 볼의 개수를 나타내는 정수,
        이렇게 총 세 개의 정수가 빈칸을 사이에 두고 주어진다.

    - 출력
        첫 줄에 영수가 생각하고 있을 가능성이 있는 답의 총 개수를 출력한다.

    - 예제 입력
        4
        123 1 1
        356 1 0
        327 2 0
        489 0 1

    - 예제 출력
        2

*/
import java.util.HashSet;
import java.util.Set;

public class Main {

    public static void main(String[] args) throws Exception {
        // 입력을 위한 준비
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine().trim());

        Set<Integer> possibleNumbers = new HashSet<>();
        for (int i = 123; i < 1000; i++) {
            String num = String.valueOf(i);
            // 숫자가 0을 포함하지 않고 모든 자리의 숫자가 서로 다른 경우에만 유효
            if (num.charAt(0) != '0' && num.charAt(1) != '0' && num.charAt(2) != '0'
                    && num.charAt(0) != num.charAt(1) && num.charAt(0) != num.charAt(2) && num.charAt(1) != num.charAt(2)) {
                possibleNumbers.add(i);
            }
        }

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int guess = Integer.parseInt(st.nextToken()); // 추측한 숫자
            int s = Integer.parseInt(st.nextToken()); // 스트라이크 수
            int b = Integer.parseInt(st.nextToken()); // 볼 수
            String guessStr = String.valueOf(guess); // 추측한 숫자를 문자열로 변환

            Set<Integer> newPossible = new HashSet<>();
            // 가능한 숫자들을 검토하여 조건에 맞는 숫자만 새로운 가능한 목록에 추가
            for (int num : possibleNumbers) {
                String numStr = String.valueOf(num); // 현재 가능한 숫자를 문자열로 변환
                int bulls = 0, cows = 0;
                for (int j = 0; j < 3; j++) {
                    if (guessStr.charAt(j) == numStr.charAt(j)) {
                        bulls++; // 위치와 숫자가 모두 맞는 경우 (스트라이크)
                    } else if (numStr.contains(String.valueOf(guessStr.charAt(j)))) {
                        cows++; // 숫자는 맞지만 위치가 틀린 경우 (볼)
                    }
                }
                if (bulls == s && cows == b) {
                    newPossible.add(num); // 조건에 맞으면 새로운 가능한 숫자 목록에 추가
                }
            }
            possibleNumbers.retainAll(newPossible); // 가능한 숫자들을 최신 정보로 갱신
        }

        System.out.println(possibleNumbers.size()); // 최종적으로 가능한 숫자의 수를 출력
    }
}

