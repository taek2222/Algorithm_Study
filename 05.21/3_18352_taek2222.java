import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/*
    https://www.acmicpc.net/problem/18352

    어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다.
    모든 도로의 거리는 1이다.

    이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서,
    최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오.
    또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.

    예를 들어 N=4, K=2, X=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.

    이 때 1번 도시에서 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 2인 도시는 4번 도시 뿐이다.
    2번과 3번 도시의 경우, 최단 거리가 1이기 때문에 출력하지 않는다.

    첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다.
    (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N)
    둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다.
    이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다.
    (1 ≤ A, B ≤ N) 단, A와 B는 서로 다른 자연수이다.

    X로부터 출발하여 도달할 수 있는 도시 중에서,
    최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.

    이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.
*/
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int INF = -1; // 무한을 나타내는 값으로, 초기 거리 불가능을 의미

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()); // 도시의 개수
        int m = Integer.parseInt(st.nextToken()); // 도로의 개수
        int k = Integer.parseInt(st.nextToken()); // 목표 거리
        int x = Integer.parseInt(st.nextToken()); // 출발 도시

        // 각 도시에서 다른 도시로 가는 경로를 저장할 리스트 배열
        List<Integer>[] edges = new List[n + 1];
        for (int i = 1; i <= n; i++) {
            edges[i] = new ArrayList<>();
        }

        // 도로 정보 입력
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            edges[a].add(b);
        }

        // 각 도시별 최단 거리 정보
        int[] dist = new int[n + 1];
        Arrays.fill(dist, INF);
        Queue<Integer> q = new ArrayDeque<>();
        q.add(x);
        dist[x] = 0; // 출발 도시의 거리는 0

        // 결과를 저장할 리스트
        List<Integer> answer = new ArrayList<>();

        // BFS 실행
        while (!q.isEmpty()) {
            int cur = q.poll();

            // 현재 거리가 k보다 크면 더 이상 탐색할 필요 없음
            if (dist[cur] > k) break;

            // 현재 거리가 k일 경우 결과 리스트에 추가
            if (dist[cur] == k) answer.add(cur);

            // 현재 도시에서 갈 수 있는 도시들 탐색
            for (int next : edges[cur]) {
                if (dist[next] != INF) continue; // 이미 방문한 도시는 스킵
                dist[next] = dist[cur] + 1; // 거리 갱신
                q.add(next); // 큐에 추가
            }
        }

        // 결과 출력
        Collections.sort(answer); // 오름차순 정렬
        StringBuilder sb = new StringBuilder();
        if (answer.isEmpty()) {
            sb.append(-1); // 결과가 없을 경우 -1 출력
        } else {
            for (int cur : answer) {
                sb.append(cur).append('\n');
            }
        }
        System.out.print(sb);
    }
}
