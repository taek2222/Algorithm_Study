// 백준 1969 DNA
// https://www.acmicpc.net/problem/1969

/* DNA의 개수와 길이를 입력받아 
   DNA의 정보를 받은 후 Hamming Distance를 통해 문자의 개수를 구한다.
   * Hamming Distance : 각 위치의 뉴클오티드 문자가 다른 것의 개수이다.
   ex) AGCAT
       GGAAT
       ------
       10100 -> 1 + 0 + 1 + 0 + = 2
 */
/*
주의
- 첫째 줄에 Hamming Distance의 합이 가장 작은 DNA 출력
- 둘째 줄에 Hamming Distance 합을 출력
- 출력시 사전순으로 가장 앞서는 것을 출력
*/

using System;
using System.Linq;

namespace Baekjoon
{
    class Program
    {
        static void Main(string[] args)
        {
            // DNA 첫글자 입력받기 갯수와 길이
            string[] inputs = Console.ReadLine().Split(' ');
            // N개와 M의 길이
            int N = int.Parse(inputs[0]);
            int M = int.Parse(inputs[1]);

            // DNA 입력 리스트
            string[] DNAS = new string[N];
            // 사용자로부터 N개의 DNA 문자열을 입력받아 배열에 저장
            for (int i = 0; i < N; i++)
            {
                DNAS[i] = Console.ReadLine();
            }

            /*  N / M ------>
                | TATGATAC
                | TAAGCTAC
                | AAAGATCC
                | TGAGATAC
                | TAAGATGT
                -------------
                  11101111  = > 7
            */

            string resultDNA = ""; // 결과 DNA 문자열을 저장할 변수
            int HDSum = 0;   // Hamming Distance의 총 합

            // 각 문자열의 위치마다 반복
            for (int i = 0; i < M; i++)
            {
                // A, C, G, T, 의 등장 횟수를 저장
                int[] count = new int[4];

                // 뉴클레오티드를 확인하고 카운트 증가하기
                foreach (var nucleotide in DNAS)
                {
                    // 현재 열의 문자에 따라 해당하는 카운트 증가
                    switch(nucleotide[i])
                    {
                        case 'A':
                            count[0]++;
                            break;
                        case 'C':
                            count[1]++; 
                            break;
                        case 'G':
                            count[2]++;
                            break;
                        case 'T':
                            count[3]++;
                            break;
                    }
                }
                // 가장 많이 등장한 뉴클레오티드의 인덱스를 찾기
                int maxindex = Array.IndexOf(count, count.Max());
                // N - 많이 나온 DNA 문자열
                HDSum += N - count[maxindex];
                // 결과 DNA에 가장 많이 나오 문자 추가
                resultDNA += "ACGT"[maxindex];
            }
            Console.WriteLine(resultDNA);
            Console.WriteLine(HDSum);
        }
    }
}
