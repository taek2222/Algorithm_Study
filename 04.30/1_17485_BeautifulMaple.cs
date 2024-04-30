// 백준 17485
//https://www.acmicpc.net/problem/17485

/*
지구 -> 달로 가는 경우
- 5시, 6시, 7시 방향으로 위에서 아래로 내려간다.
5시 방향, 6시 방향, 7시 방향으로 총 3가지 방향으로 갈 수 있다.
x x x
  o
* 목적지에서 올 수 있는 방법도 3가지가 된다.
같은 방향으로 두번 연속으로 움직일 수 없다
5시-> 5시 X, 5시 -> 6시 O
* 연료를 최대한 아끼면서 가는 방법을 채택해야한다.
각 이동 하는 칸에는 [1 2 3] 3가지 방향을 가지고 잇음
 */

using System;
using System.Linq;
using System.Runtime.Intrinsics.Arm;

namespace Baekjoon
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int N = input[0];
            int M = input[1];

            int[,] Map = new int[N, M];
            for (int i = 0; i < N; i++)
            {
                var line = Console.ReadLine().Split().Select(int.Parse).ToArray();
                for (int j = 0; j < M; j++)
                {
                    // 각 i라인으로 j 수 만큼 입력 받기
                    Map[i,j] = line[j];
                }
            }

            // DP 배열 초기화 및 계산
            int result = MinDP(N, M, Map);

            Console.WriteLine(result);
        }


        static int MinDP(int N, int M, int[,] map)
        {
            int[,,] DP = new int[N, M, 3];
            int INF = int.MaxValue;

            // DP 배열 초기화
            for(int i = 0;i < N;i++)
                for(int j = 0;j < M; j++)
                    for(int k = 0;k < 3; k++)
                        DP[i,j,k] = (i == 0) ? map[i,j] : INF;

            // DP로 사용하여 각 위치까지의 최소 연료 소비량 계산하기
            for(int i = 1; i < N; i++)
            {
                for(int j = 0; j < M; j++)
                {
                    /// 왼쪽 대각선에서 올 경우
                    if (j > 0) DP[i, j, 0] = Math.Min(DP[i, j, 0], 
                        map[i, j] + Math.Min(DP[i - 1, j - 1, 1], DP[i - 1, j - 1, 2]));
                    // 위에서 올 경우
                    DP[i, j, 1] = Math.Min(DP[i, j, 1], 
                        map[i, j] + Math.Min(DP[i - 1, j, 0], DP[i - 1, j, 2]));
                    // 오른쪽 대각선에서 올 경우
                    if (j < M - 1) DP[i, j, 2] = Math.Min(DP[i, j, 2], 
                        map[i, j] + Math.Min(DP[i - 1, j + 1, 0], DP[i - 1, j + 1, 1]));
                }
            }
            // 마지막 행에서의 최소값 찾기
            int minFuel = INF;
            for (int j = 0; j < M; j++)
                for (int k = 0; k < 3; k++)
                    // 마지막 행(N-1)의 모든 위치에서의 연료 소비량 중 최소값을 찾습니다.
                    minFuel = Math.Min(minFuel, DP[N - 1, j, k]);

            return minFuel;
        }
    }
}
