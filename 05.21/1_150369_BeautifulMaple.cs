public class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        // 결과값을 저장할 변수
        long result = 0;
        
        // 현재 남아있는 배달량과 픽업량을 추적할 변수
        int delnum = 0;
        int picnum = 0;

        // 가장 먼 집(n-1)부터 시작하여 첫 번째 집(0)까지 순회
        for (int i = n - 1; i >= 0; i--) {
            // 해당 집에 배달이나 픽업이 필요한 경우
            if (deliveries[i] > 0 || pickups[i] > 0) {
                // 이건 찾아본 내용
                // 왕복 횟수를 추적할 변수
                int rounds = 0;
                
                // 현재 남은 배달량이나 픽업량이 해당 집의 필요량보다 적을 때
                while (delnum < deliveries[i] || picnum < pickups[i]) {
                    // 트럭 용량(cap)만큼 배달 및 픽업량을 추가
                    delnum += cap;
                    picnum += cap;
                    // 왕복 횟수 증가
                    rounds++;
                }

                // 왕복 거리 계산 (현재 집까지 왕복 거리 * 왕복 횟수)
                result += (i + 1) * 2 * rounds;
                
                // 해당 집의 배달 및 픽업을 처리한 후 남은 배달 및 픽업량 업데이트
                delnum -= deliveries[i];
                picnum -= pickups[i];
            }
        }
        
        // 총 이동 거리 반환
        return result;
    }
}
