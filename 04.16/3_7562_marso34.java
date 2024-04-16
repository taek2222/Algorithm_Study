import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int[] arrX = {-1, -2, -2, -1, 1, 2, 2, 1};
        int[] arrY = {-2, -1, 1, 2, 2, 1, -1, -2};

        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            int l = Integer.parseInt(br.readLine());

            int[][] nBoard = new int[l][l];
            boolean[][] board = new boolean[l][l];

            st = new StringTokenizer(br.readLine());

            int x = Integer.parseInt(st.nextToken()); // 현재 위치
            int y = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());

            int destX = Integer.parseInt(st.nextToken()); // 목적지
            int destY = Integer.parseInt(st.nextToken());

            
            Queue<int[]> queue = new LinkedList<>();
            queue.add(new int[] {x, y});
            board[x][y] = true;

            loop1:
            while (!queue.isEmpty()) {
                int[] pos = queue.poll();
                int posX = pos[0];
                int posY = pos[1];
                
                for (int j = 0; j < 8; j++) {
                    int tempX = posX + arrX[j];
                    int tempY = posY + arrY[j];

                    if (tempX >= 0 && tempX < l && tempY >= 0 && tempY < l && !board[tempX][tempY]) {
                        queue.add(new int[] {tempX, tempY});
                        nBoard[tempX][tempY] = nBoard[posX][posY] + 1;
                        board[tempX][tempY] = true;
                        
                        if (tempX == destX && tempY == destY) {
                            break loop1;
                        }
                    }
                }
            }
            
            System.out.println(nBoard[destX][destY]);
        }
    }
}