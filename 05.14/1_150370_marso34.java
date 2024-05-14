import java.util.Map;
import java.util.List;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Arrays;
import java.time.LocalDate;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        // 오늘 날짜
        LocalDate date = LocalDate.parse(today.replace(".", "-"));
        
        Map<String, Integer> map = new HashMap<>();
        List<Integer> list = new ArrayList<>();
        
        for (String term : terms) {
            String[] arr = term.split(" ");
            
            map.put(arr[0], Integer.parseInt(arr[1]));
        }
        
        int index = 0;
        
        for (String privacy : privacies) {
            String[] arr = privacy.split(" ");
            
            LocalDate pDate = LocalDate.parse(arr[0].replace(".", "-"));
            
            pDate = pDate.plusMonths(map.get(arr[1]));
            
            if (!date.isBefore(pDate)) {
                list.add(index);
            }
            
            index++;
        }
        
        int[] answer = new int[list.size()];
        
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i) + 1;
        }
        
        return answer;
    }
}