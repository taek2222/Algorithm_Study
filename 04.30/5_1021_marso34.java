import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.stream.IntStream;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] arr = new int[m];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < m; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        LinkedList<Integer> queue = IntStream.range(1, n + 1)
                .boxed()
                .collect(Collectors.toCollection(LinkedList::new));

        /**
         * 1. queue.remove();                    // 첫번째 원소 뽑아내기
         * 2. queue.add(queue.remove())          // 왼쪽으로 한 칸 이동
         * 3. queue.addFirst(queue.removeLast()) // 오른쪽으로 한 칸 이동
         * 
         * 1 2 3 4 5 6 7 8 9 // 기준
         * 2 3 4 5 6 7 8 9 1 // 2번
         * 9 1 2 3 4 5 6 7 8 // 3번
         * 
         */

        int cnt = 0;

        loop1:
        for (int index : arr) {  
            /**
             * index의 실제 위치가 어디 있느냐에 따라서 결정
             * index가 왼쪽에 가까우면 2번
             * index가 오른쪽에 가까우면 3번
             * 2번, 3번 연산을 수행할 수록 index의 위치는 이동
             */

            while (queue.peek() != index) {
                int tIndex = queue.indexOf(Integer.valueOf(index)); // index의 실제 위치

                if (tIndex < queue.size() - tIndex) { // 2번
                    queue.add(queue.poll());
                } else { // 3번
                    queue.addFirst(queue.removeLast());
                }
                
                cnt++;
            }
            
            queue.poll(); // 1번, 반드시 수행
        }

        System.out.println(cnt);
    }
}