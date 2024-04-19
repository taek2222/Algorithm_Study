import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/*
    https://www.acmicpc.net/problem/20291

    첫째 줄에 바탕화면에 있는 파일의 개수 $N$이 주어진다.
    ($1 \leq N \leq 50\ 000$)
    둘째 줄부터
    $N$개 줄에 바탕화면에 있는 파일의 이름이 주어진다.
    파일의 이름은 알파벳 소문자와 점(.)으로만 구성되어 있다.
    점은 정확히 한 번 등장하며, 파일 이름의 첫 글자 또는 마지막 글자로 오지 않는다.
    각 파일의 이름의 길이는 최소
    $3$, 최대 $100$이다.
*/

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Map<String, Integer> map = new HashMap<>();

        // 파일 갯수 N
        int N = Integer.parseInt(br.readLine());

        String[] file;

        // 파일 갯수 만큼 반복
        for(int i = 0; i < N; i++) {
            // 파일명을 읽어와 . 기준으로 분할
            file = br.readLine().split("\\.");
            // 분할한 배열 중 2번째 요소로 값 존재 확인 후 없으면 생성 있으면 카운팅
            map.put(file[1], map.getOrDefault(file[1], 0) + 1);
        }

        // HashMap 을 리스트로 변환
        List<Map.Entry<String, Integer>> list = new ArrayList<>(map.entrySet());

        // 정렬
        list.sort(Map.Entry.comparingByKey());

        // 출력
        for(Map.Entry<String, Integer> entry : list)
            System.out.println(entry.getKey() + " " + entry.getValue());
    }
}
