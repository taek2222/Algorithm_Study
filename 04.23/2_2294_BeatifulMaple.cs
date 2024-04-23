// 백준 2294
// https://www.acmicpc.net/problem/2294

/*
  첫째 줄에 n과 k로 동전의 종류의 수 값과 목표 금액을 입력

  입력된 동전의 종류의 수만큼 동전 종류를 배열에 저장

  배열에 저장된 값이 10000를 초과하는 경우 -1를 출력
  그러지 않을 경우 사용한 동전의 최소 개수를 출력한다.
*/




using System;
using System.Runtime.Intrinsics.Arm;

namespace Baekjoon
{
    class Progrma
    {
        static void Main(string[] args)
        {
            string[] input = Console.ReadLine().Split(' ');
            int n = int.Parse(input[0]); // 동전의 종류 수
            int k = int.Parse(input[1]); // 목표 금액
            int[] coins = new int[n]; // 동전 종류를 저장할 배열

            // 동전의 종류 입력
            for (int i = 0; i < n; i++)
            {
                // 동전들 저장하기
                coins[i] = int.Parse(Console.ReadLine());
            }

            // dp 배열 초기화. dp[i]는 금액 i를 만들기 위해 필요한 최소한의 동전 수를 저장.
            // 10001은 임의로 설정한 "불가능"을 뜻하는 값. (최대 k가 10000이므로)
            int[] dp = Enumerable.Repeat(10001, k + 1).ToArray();
            dp[0] = 0; // 0원을 만드는 데 필요한 동전의 수는 0개
            for (int i = 0; i < n; i++)
            {
                // 현재 동전으로 목표금액까지
                for (int j = coins[i]; j <= k; j++)
                {
                    // 기존에 계산된 값(dp[j])과 현재 동전을 사용했을 때의 값(dp[j - coins[i]] + 1) 중 더 작은 값으로 갱신
                    if (dp[j - coins[i]] != 10001)
                    {
                        dp[j] = Math.Min(dp[j], dp[j - coins[i]] + 1);
                    }
                }
            }
            // 금액이 아닌 경우 -1 출력
            if (dp[k] == 10001)
            {
                Console.WriteLine(-1); // 결과 출력
                
            }
            else
            {
                // 목표 금액을 만들 수 있는 최소 동전 수 출력
                Console.WriteLine(dp[k]);
            }
        }
    }
}
