import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        Integer[] crane = new Integer[n];

        for (int i = 0; i < n; i++) {
            crane[i] = Integer.parseInt(st.nextToken());
        }

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        ArrayList<Integer> weight = new ArrayList<>();
        
        for (int i = 0; i < m; i++) {
            weight.add(Integer.parseInt(st.nextToken()));
        } // 여기까지 입력

        // 내림차순 정렬
        Arrays.sort(crane, Comparator.reverseOrder()); 
        weight.sort(Collections.reverseOrder()); 

        int cnt = 0;

        if (crane[0] < weight.get(0)) { // 크레인으로 옮길 수 없으면
            bw.write("-1");
            bw.flush();   //남아있는 데이터를 모두 출력시킴
            bw.close();   //스트림을 닫음
            return;
        }
        
        while(!weight.isEmpty()) {
            int i = 0;

            for (int c : crane) {
                if (weight.isEmpty()) { // 옮기던 도중 끝나면
                    break;
                }
                
                for (; i < weight.size(); i++) {
                    if (c >= weight.get(i)) { // 크레인으로 옮길 수 있으면
                        weight.remove(i);
                        break;
                    }
                }
            }
            
            cnt++;
        }
    
        bw.write(cnt + "");
        bw.flush();   //남아있는 데이터를 모두 출력시킴
        bw.close();   //스트림을 닫음
    }
}