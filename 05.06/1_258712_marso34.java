import java.util.HashMap;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int n = friends.length;
        
        int[][] arr = new int[n][n];   // 주고받은 선물 표. [준 사람][받은 사람]
        int[] giftDegree = new int[n]; // 선물지수
        
        HashMap<String, Integer> map = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            map.put(friends[i], i); // 이름 순서대로 0 ~ n        
        }
        
        for (String gift : gifts) {
            String[] f = gift.split(" ");
                        
            giftDegree[map.get(f[0])]++; // 준 선물
            giftDegree[map.get(f[1])]--; // 받은 선물            
            arr[map.get(f[0])][map.get(f[1])]++;
        } // 여기까지 주고 받은 기록(arr), 선물 지수(giftDegree) 세팅

        int answer = 0;
        
        for (int i = 0; i < n; i++) {
            int num = 0;
            
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    continue;
                }    
                
                // 더 많이 선물을 줌 || 주고 받은 수 같고 선물 지수가 높다면  
                if (arr[i][j] > arr[j][i] || (arr[i][j] == arr[j][i] && giftDegree[i] > giftDegree[j])) {
                        num++;
                }
            }
            
            if (answer < num) {
                answer = num;
            }
        }
        
        return answer;
    }
}