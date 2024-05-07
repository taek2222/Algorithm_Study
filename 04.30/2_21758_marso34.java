import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        long[] arr = new long[n];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        } // 여기까지 입력

        long max = 0;

        /**
         * 
         * 1번 방법. 모든 경우의 수에서 가장 큰 수 찾기
         * 
        for(int i = 0; i < n-1; i++) {
            for(int j = i+1; j < n; j++) {
                // 벌통 장소
                for (int k = 0; k < n; k++) { 
                    if (i == k || j == k) {
                        continue;
                    }
                    
                    // 모든 인덱스를 활용하지 않을 경우 // 없으면 11점, 있으면 24점
                    if (!(i == 0 && k == n-1) && !(k == 0 && j == n-1) && !(i == 0 && j == n-1)) {
                        continue;
                    }
                    
                    // 꿀 양 계산
                    // i ~ k까지 꿀 + j ~ k까지 꿀 
                     
                    int index1 = i; 
                    int index2 = j;
                    
                    long sum = 2* arr[k] - arr[i] - arr[j]; // 2 * 도착지점 - (두 출발 지점)

                    // 출발지점부터 도착지점 이전 까지 sum
                    // 원래 목표: 출발지 제외 도착지점까지 sum
                    while (index1 != k || index2 != k) {
                        if (index1 != k) {
                            if (index1 != j) {
                                sum += arr[index1];
                            }
                            
                            index1 = (i > k) ? index1-1 : index1+1;
                        }

                        if (index2 != k) {
                            if (index2 != i) {
                                sum += arr[index2];
                            }
                            
                            index2 = (j > k) ? index2-1 : index2+1;
                        }
                    }
                    
                    if (sum > max) {
                        max = sum;
                    } 
                }
            }
        }
         */
        
        /**
         * 2번 방법, 55점
         * i, j는 벌, k는 벌통 (i, j는 순서 상관 X) * i, j 값은 연산에서 제거
         * 
         * i 왼쪽 고정 => j 오른쪽 고정 => k 선택
         * i 왼쪽 고정 => k 오른쪽 고정 => j 선택
         * k 왼쪽 고정 => j 오른쪽 고정 => i 선택
         * 
         * 각 케이스마다 반복문 했을때도 55점, 속도는 더 느림  
         * 
        for (int index = 1; index < n-1; index++) {
            long sum1 = arr[index]; // 미리 중복 값 처리
            long sum2 = -arr[index];
            long sum3 = -arr[index];

            for (int i = 0; i < n; i++) {
                // index가 k일 경우
                // 1 ~ k   합
                // k ~ n-1 합
                if (i > 0 && i < n-1) {
                    sum1 += arr[i];
                }

                // index가 j일 경우
                // 1 ~ n 합-j
                // j+1 ~ n 합
                if (i > 0) {
                    if (i > index) { // j+1 ~ n
                        sum2 += arr[i];
                    }

                    sum2 += arr[i];
                }

                // index가 i일 경우
                // 0 ~ i-1 합
                // 0 ~ n-1 합-i
                if (i < n-1) {
                    if (i < index) { // j+1 ~ n
                        sum3 += arr[i];
                    }

                    sum3 += arr[i];
                }
            }

            if (sum1 > max) {
                max = sum1;
            }

            if (sum2 > max) {
                max = sum2;
            }

            if (sum3 > max) {
                max = sum3;
            }
        }
         */  

        /**
         * 3번 방법, 드디어 100점
         * 
         * 2번 방법과 개념은 동일하되 미리 배열의 누접합을 계산
         * i 왼쪽 고정 => j 오른쪽 고정 => k 선택
         * i 왼쪽 고정 => k 오른쪽 고정 => j 선택
         * k 왼쪽 고정 => j 오른쪽 고정 => i 선택
         * 
         */
        long[] left = new long[n];
        long[] right = new long[n];

        left[0] = arr[0];       // 오름차순 
        right[n-1] = arr[n-1];  // 내림차순 

        for (int i = 1; i < n; i++) {
            left[i] = left[i-1] + arr[i];
            right[n-i-1] = right[n-i] + arr[n-i-1];
        }

        for (int index = 1; index < n-1; index++) {
            // index가 k일 경우
            // 1 ~ k   합
            // n-1 ~ k 합
            long sum1 = left[index] - arr[0] + right[index] - arr[n-1];

            // index가 j일 경우
            // 1 ~ n 합-j
            // j+1 ~ n 합
            long sum2 = left[n-1] - arr[0] - arr[index] + left[n-1] - left[index];         

            // index가 i일 경우
            // i-1 ~ 0 합
            // n-2 ~ 0 합-i
            long sum3 = right[0] - right[index] + right[0] - arr[n-1] - arr[index];

            if (sum1 > max) 
                max = sum1;

            if (sum2 > max)
                max = sum2;
            
            if (sum3 > max)
                max = sum3;
        }

        System.out.println(max);
    } 
}