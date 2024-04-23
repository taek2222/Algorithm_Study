import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] cntArr = new int[n];
        
        ArrayList<String> keyword = new ArrayList<>();
        HashMap<String, Integer> map = new HashMap<>(); 

        int value = 0;
        
        for (int i = 0; i < n; i++) {
            String str = br.readLine().split("\\.")[1];

            if (map.get(str) == null) {
                map.put(str, value);
                keyword.add(str);
                cntArr[value]++;
                value++;
            } else {
                cntArr[map.get(str)]++;
            }
        }
        
        Collections.sort(keyword);

        for (String str : keyword) {
            System.out.println(str + " " + cntArr[map.get(str)]);
        }
    }
}