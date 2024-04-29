// 백준 1021
//https://www.acmicpc.net/problem/1021

/*
 10 3
 1 2 3
1. [1][2][3][4~10]
    1
 ->[1][2][3] -> [2][3] 1은 지민이가 뽑았기 때문에 삭제
 ->[2][3] -> [3] 2는 지민이가 뽑았기 때문에 삭제
 ->[3] -> [] 3은 지민이가 뽑았기 때문에 삭제
회전을 하지 않았기 때문에 0

 10 3
 2 9 5
2. [1][2][3][4][5][6][7][8][9][10]
// 반으로 나누었을 때 가장 짧은 쪽 기준으로 회전시키기
[2] -> [2][3][4][5][6][7][8][9][10][1] -> [3][4][5][6][7][8][9][10][1]
[9] -> [3][4][5][6][7][8][9][10][1] -> [1][3][4][5][6][7][8][9][10] -> [10][1][3][4][5][6][7][8]
[5] -> [10][1][3][4][5][6][7][8] -> [8][10][1][3][4][5][6][7] -> [7][8][10][1][3][4][5][6]
->[6][7][8][10][1][3][4][5]
총 8번
 */

using System;
using System.Collections.Generic;
using System.Linq;

namespace Baekjoon
{
    class Program
    {
        static void Main(string[] args)
        {
            // 파일의 개수 입력 받기
            int N = int.Parse(Console.ReadLine());
            // 확장자 별 파일 수를 세기 위한 사전
            // <확장자 이름(key), 카운트(Value)> 값이 들어갈 예정
            Dictionary<string, int> extensionCount = new Dictionary<string, int>();

            for (int i = 0; i < N; i++)
            {
                // 파일 이름 입력 받기
                string FileName = Console.ReadLine();
                // 확장자 분리하기
                string extension = FileName.Split('.')[1];

                // 이미 사전에 해당 확장자가 존재한다면, 해당 확장자의 값(파일 수)를 1 증가
                if (extensionCount.ContainsKey(extension))
                {
                    extensionCount[extension]++;
                }
                else
                {
                    // 사전에 해당 확장자가 존재하지 않는다면, 새로운 항목을 추가하고 파일 수를 1로 설정
                    extensionCount.Add(extension, 1);
                }
            }
            // 오름차순으로 정렬
            var sortExtensions = extensionCount.OrderBy(x => x.Key);

            // 오름차순으로 확장자와 파일 수를 출력하기
            foreach (var ext in sortExtensions)
            {
                Console.WriteLine($"{ext.Key} {ext.Value}");
            }
        }
    }
}
