/* 백준 문제 링크
 https://www.acmicpc.net/problem/11047

 문제
 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
*/

/* 
 첫 번째 줄에 N과 K가 주어진다.
 ex) 10 4200
 가지고 있는 동전의 종류 : N
 동전을 이용한 목표 금액 : K
 두 번째 줄에 N개의 줄에 동전의 가치가 오름차순으로 주어진다.
 ex)
 5
 10
 50
 100 ...

 동전을 최소한으로 사용한 값을 출력한다.
 사용한 알고리즘 : 욕심쟁이 알고리즘 (탐욕의 알고리즘 - Greedy Algorithm)
 */

using System;

namespace Baekjoon
{
    class Progrma
    {
        static void Main(string[] args)
        {
            int count = 0; //동전 카운트
            string[] input = Console.ReadLine().Split();

            // 동전의 종류 :N, 목표 금액 : K
            int N = int.Parse(input[0]);
            int K = int.Parse(input[1]);

            // 동전의 종류만큼 동전의 가치를 저장하기
            int[] values = new int[N];

            // 동전의 종류 수만큼 반복하여 저장하기
            for (int i = 0; i < N; i++)
            {
                values[i] = int.Parse(Console.ReadLine());
            }

            // 목표 금액이 0이 될 때까지 반복
            while (K != 0) 
            {
                // 가장 큰 가치의 동전부터 시작하여 목표 금액에서 빼볼 수 잇는지
                for (int i = N -1; i >= 0; i--)
                {
                    // 목표 금액에서 뺄 수 있는 경우
                    if(K - values[i] >= 0)
                    {   
                        // 목표 금맥에서 현재 동전의 가치를 뺍니다
                        K -= values[i];
                        // 사용한 동전의 개수를 1 증가
                        count++;
                        break; //또 뺄 수 있기 때문에 빠져나갑니다.
                    }
                }
            }
            // 목표 금액을 만드는 데 필요한 동전의 최소 개수를 출력하기
            Console.WriteLine(count);
        }
    }
}
