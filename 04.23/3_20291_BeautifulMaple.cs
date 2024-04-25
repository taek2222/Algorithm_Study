// 백준 20291
// https://www.acmicpc.net/problem/20291

/*
  사전순으로 확장자를 정리하여 각 몇 개씩 있는지 출력하는 문제
  구문자 기준으로 확장자가 나타나기 때문에 이 확장자를 저장할 용도가 필요
  ex)abc.txt
  
  Dictionary<확장자 이름(key), 카운트(Value)> 사전형 데이터로 배열을 다루는 클래스
  

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
