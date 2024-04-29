// 백준 1092
// https://www.acmicpc.net/problem/1092

// 각 크레인을 이용하여 박스를 옮기는 작업
// 각 크레인 별로 박스를 들 수 있는 힘이 있지만 그 힘을 넘어가는 무게는 들지 못한다.
// 내림차순을 이용하여 가장 힘이 좋은 크레인으로 무거운 박스를 배에 옮기기 좋다고 판단

/*
            3 -> 6 8 9
            5 -> 2 5 2 4 7
            출력 -> 2
            
            대안 1
            9 8 6
            | | |
            7 5 4 2 2
            내림차순으로 무거운 박스를 옮김

            다 못 옮기면 -1
*/

using System;
using System.Runtime.Intrinsics.Arm;

namespace Baekjoon
{
    class Progrma
    {
        static void Main(string[] args)
        {
            // 테스트 케이스 개수 입력 받기 (첫번째)
            int N = int.Parse(Console.ReadLine());  // N : 크레인
            // 입력 -> 공백에 따라 문자열 분리 -> 정수로 변환 후 리스트 요소로 변환 -> 내림차순 -> 리스트로 변환
            List<int> Cranes = Console.ReadLine().Split(' ').Select(int.Parse).OrderByDescending(n => n).ToList();

            int M = int.Parse(Console.ReadLine());  // M : 박스의 수
            List<int> Boxes = Console.ReadLine().Split(' ').Select(int.Parse).OrderByDescending(n => n).ToList();

            // 다 못 옮기는 경우
            if (Boxes[0]> Cranes[0])
            {
                Console.WriteLine("-1");
                return;
            }

            // 수행되는 시간 카운트
            int time = 0;
            while (Boxes.Count > 0)
            {
                int idx = 0;
                // 박스를 크레인으로 옮기기
                for(int i = 0; i < Cranes.Count;)
                {
                    // 다 옮기면 끝내기
                    if (idx == Boxes.Count) break;
                    if (Cranes[i] >= Boxes[idx])
                    {
                        // 조건 만족시 하나 삭제
                        Boxes.RemoveAt(idx);
                        //현재 크레인으로 다 옮겼을 경우
                        i++;
                    }
                    else
                    {
                        // 카운트 증가
                        idx++;
                    }
                }
                // 크레인 다 사용했다면 1 증가
                time++;
            }

            Console.WriteLine(time);
        }
    }
}
