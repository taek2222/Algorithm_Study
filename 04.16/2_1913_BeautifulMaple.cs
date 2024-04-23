// 백준 1913문제
// https://www.acmicpc.net/problem/1913
/*
  달팽이 패턴을 (n x n) 중앙에서 시작하여
  위 -> 오른쪽 -> 아래 -> 왼쪽 순서로 회전하는 패턴을 그리고 있다.
  x좌표와 y좌표가 (n x n)판에 벗어나지 않고 숫자 1부터 하나씩 증가해야한다.
*/


// 제출하는 과정에서 좌표값을 출력 ex) (5, 7) 형태와 많은 반복문으로 시간초과
// StringBuilder sb = new StringBuilder();를 통해서 좌표값을 문자로 받아 처리

// 완성된 코드
using System;
using System.Text;

namespace Baekjoon
{
    class Program
    {
        static void Main(string[] args)
        {
            // 결과를 효율적으로 저장하기 위한 StringBuilder
            StringBuilder sb = new StringBuilder();
            // NxN 배열의 크기값 받아오기
            int N = int.Parse(Console.ReadLine()); // NxN 배열
            // 찾고자 하는 대상 좌표
            int target = int.Parse(Console.ReadLine()); // 찾고자 하는 수

            // 달팽이 모양을 나타내는 2차원 배열 초기화 및 선언
            int[,] snail = new int[N, N];
            // 현재 위치 (x, y)와 방향을 나타내는 변수들을 초기화
            // 왼쪽 상단에서 시작(0,0)
            int x = 0, y = 0, dir = 0;

            // 방향을 제어하는 배열 (상, 우, 하, 좌)
            int[] dx = { 1, 0, -1, 0 }; 
            int[] dy = { 0, 1, 0, -1 };

            // 배열 안의 총 요소 개수
            int num = N * N;

            // 달팽이 패턴
            while (num > 0)
            {
                // 현재 위치에 현재 숫자를 채웁니다.
                // 좌표 안에 숫자
                snail[x, y] = num;

                // 다음 위치를 현재 방향에 따라 계산
                int nx = x + dx[dir];
                int ny = y + dy[dir];

                // 다음 위치가 유효하고 비어 있으면 해당 위치로 이동합니다.
                // 찾아본 구간 : n x n를 벗어나지 않게 하기 위해서
                if (nx >= 0 && nx < N && ny >= 0 && ny < N && snail[nx, ny] == 0)
                {
                    x = nx;
                    y = ny;
                }
                else // 방향을 변경하고 그에 따라 이동합니다.
                {
                    dir = (dir + 1) % 4;
                    x += dx[dir];
                    y += dy[dir];
                }

                // 채워야 할 숫자를 감소
                num--;
            }

            // 대상 숫자의 위치를 저장할 변수들을 초기화합니다.
            int targetX = 0, targetY = 0;

            // 달팽이 배열을 순회하여 대상 숫자를 찾고 해당 위치를 저장합니다.
            for (int i = 0; i < N; i++)
            {
                for (int j = 0; j < N; j++)
                {
                    if (snail[i, j] == target)
                    {
                        targetX = i + 1; // 1부터 시작하는 인덱스에 맞게 조정
                        targetY = j + 1; // 1부터 시작하는 인덱스에 맞게 조정
                    }
                    sb.Append(snail[i, j] + " "); // 현재 요소를 결과 StringBuilder에 추가합니다.
                }
                sb.Append("\n"); // 각 행 뒤에 줄 바꿈을 추가합니다.
            }

            // 대상 숫자의 위치를 결과 StringBuilder에 추가합니다.
            sb.Append(targetX + " " + targetY);

            // 결과를 출력합니다.
            Console.Write(sb.ToString());
        }
    }
}
