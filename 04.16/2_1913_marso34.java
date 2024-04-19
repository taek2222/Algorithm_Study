import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        // System.out.println 사용하면 메모리 초과

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        int x = 0;
        int y = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int value = getValue(i, j, n);

                if (value == m) {
                    x = i + 1;
                    y = j + 1;
                }

                bw.write(value+" ");
            }

            bw.write("\n");
        }

        bw.write(x + " " + y +"\n");

        bw.flush();   //남아있는 데이터를 모두 출력시킴
        bw.close();   //스트림을 닫음
    }

    public static int getValue(int i, int j, int n) {
        // 25 10 11 12 13
        // 24  9  2  3 14
        // 23  8  1  4 15
        // 22  7  6  5 16
        // 21 20 19 18 17

        // (0,0) (0,1) (0,2) (0,3) (0,4) 
        // (1,0) (1,1) (1,2) (1,3) (1,4) 
        // (2,0) (2,1) (2,2) (2,3) (2,4) 
        // (3,0) (3,1) (3,2) (3,3) (3,4) 
        // (4,0) (4,1) (4,2) (4,3) (4,4) 

        // 0 0 0 0 0 // depth
        // 0 1 1 1 0 
        // 0 1 2 1 0 
        // 0 1 1 1 0 
        // 0 0 0 0 0 

        // 2 2 2 2 2 // revDepth
        // 2 1 1 1 2 
        // 2 1 0 1 2 
        // 2 1 1 1 2 
        // 2 2 2 2 2

        int dx = i > n/2 ? n - i -1 : i;
        int dy = j > n/2 ? n - j -1 : j;
        
        int maxDepth = n/2;
        int depth = dx > dy ? dy : dx;   // 오름차순, 바깥부터 0
        int revDepth = maxDepth - depth; // 내림차순, 바깥부터 maxDepth
        
        int value = i+j - depth*2;
        
        value = i <= j ? value : revDepth * 8 - value;
        
        if (value != 0) {
            revDepth--;
        }
        
        int k = revDepth * 2 + 1;

        return value + k * k;
    }
}

/*

// 예전에 풀어본 비슷한 유형 문제
// 아래 같은 형태
// 21 22 23 24 25 
// 20  7  8  9 10 
// 19  6  1  2 11 
// 18  5  4  3 12 
// 17 16 15 14 13

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        int left, right, top, bottom, index;
        left = top = 0;
        right = m-1;
        bottom = n-1;
        index = n * m;
        
        int[][] spiralArr = new int[n][m];
        
        while (left <= right && top<= bottom) {
            for (int j = right; j > left; j--) {
                spiralArr[top][j] = index;
                index--;
            }
            for (int i = top; i < bottom; i++) {
                spiralArr[i][left] = index;
                index--;
            }
            for (int j = left; j < right; j++) {
                spiralArr[bottom][j] = index;
                index--;
            }
            for (int i = bottom; i > top; i--) {
                spiralArr[i][right] = index;
                index--;
            }
            
            if(left == right && right == top && top == bottom)
                spiralArr[top][left] = index;
            
            left = left + 1;
            right = right - 1;
            top = top + 1;
            bottom = bottom - 1;
        }
        
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++)
                System.out.printf("%2d ", spiralArr[i][j]);
            System.out.println();
        }
    }
}

*/