import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    static class CustomTime<T extends Comparable<T>> implements Comparable<CustomTime<T>> {
        private T time;
        private boolean isStart;

        CustomTime(T time, boolean isStart) {
            this.time = time;
            this.isStart = isStart;
        }

        public T getTime() {
            return time;
        }

        public boolean getIsStart() {
            return isStart;
        }

        @Override
        public int compareTo(CustomTime<T> other) {
            return this.time.equals(other.time) ? Boolean.compare(this.isStart, other.isStart) : this.time.compareTo(other.time);
        }
    } 

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        ArrayList<CustomTime<Long>> list = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            long start = Long.parseLong(st.nextToken());
            long end = Long.parseLong(st.nextToken());

            list.add(new CustomTime(start, true));
            list.add(new CustomTime(end, false));
        }

        Collections.sort(list);

        int cnt = 0;
        int max = 0;
                
        for (CustomTime ct : list) {
            if (ct.getIsStart()){
                cnt += 1;
                max = Math.max(cnt, max);
            }
            else 
                cnt -= 1;
        }
        
        System.out.println(max);
    }
}