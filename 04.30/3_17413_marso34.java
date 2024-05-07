import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String input = br.readLine();

        int index = 0;
        int startIdx = 0;
        int endIdx = -1;

        Queue<String> queue = new LinkedList<>();
        LinkedList<Boolean> list = new LinkedList<>();

        /**
         * 
         * <> 단위로 queue에 삽입
         * 
         * ex) <open>tag<close>일 경우
         *     <open>
         *     tag
         *     <close>    queue에 삽입
         * 
         * <> 없으면 queue에 하나에 삽입
         * <> 없는 경우 공백 단위로 split후 뒤집기
         * <> 여부는 list로 판단, true면 <>
         * 
         */

        for (char ch : input.toCharArray()) {
            if (ch == '<') {
                startIdx = index;
                
                if (startIdx != 0 && startIdx-1 != endIdx) { // 두번째 괄호부터 
                    queue.add(input.substring(endIdx+1, startIdx));
                    list.add(false);
                }
            } else if (ch == '>') {
                endIdx = index;

                queue.add(input.substring(startIdx, endIdx+1));
                list.add(true);
            } else if (index == input.length()-1) {
                queue.add(input.substring(endIdx+1));
                list.add(false);
            }

            index++;
        }

        while (queue.size() > 0) { // 출력
            if (list.poll()) {
                System.out.print(queue.poll());
            } else {                
                String[] arr = queue.poll().split(" ");
                
                for (int i = 0; i < arr.length; i++) {
                    StringBuilder temp = new StringBuilder(arr[i]).reverse();

                    if (i != arr.length-1)
                        temp.append(" ");
                        
                    System.out.print(temp);
                }
            }
        }
    }
}