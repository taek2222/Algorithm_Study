// 백준 19598 문제
// https://www.acmicpc.net/problem/19598

/* 
N개의 회의를 진핼 할 수 있는 최소 회의실 개수를 구하는 미션
단, 회의는 중간에 끝날 수 없고, 회의가 끝나는 동시에 다음 회의가 시작할 수 있다.
또한 회의의 시간은 끝나는 시간보다 항상 작다.
*/

// 시간을 정렬하기
// 시간을 리스트에서 넣고 뺄 수 있게 하기

// 안 풀려서 찾아본 결과 정렬식을 람다식으로 간단하게 표현할 수 있었다.
// meetings.Sort((a, b) => a.time == b.time ? a.type.CompareTo(b.type) : a.time.CompareTo(b.time));


using System;
using System.Collections;
using System.Collections.Generic;

namespace Baekjoon
{
    class Program
    {
        static void Main(string[] args)
        {
            // 최소 회의실 개수 입력하기
            int N = int.Parse(Console.ReadLine());

            // 시작 시간과 끝나는 시간를 저장할 리스트
            List<(int time, int type)> meetings = new List<(int time, int type)>();
            
            // N개의 회의 시간을 입력 받아 시간 메모하기
            for (int i = 0; i < N; i++) 
            {
                string[] T_Input = Console.ReadLine().Split();
                int T_start = int.Parse(T_Input[0]);
                int T_end = int.Parse(T_Input[1]);
                meetings.Add((T_start, 1)); // 시작 이벤트 (시간, 타입), 여기서 타입 1은 시작을 의미
                meetings.Add((T_end, -1)); // 종료 이벤트 (시간, 타입), 여기서 타입 -1은 종료를 의미
            }

            // 회의 시간순으로 정렬, 시간이 같다면 종료 회의 시간이 먼저 오도록
            /*  ex)
                (1, 1) - 회의 A 시작
                (2, 1) - 회의 C 시작
                (3, -1) - 회의 A 종료
                (3, 1) - 회의 B 시작
                (4, -1) - 회의 C 종료
                (5, -1) - 회의 B 종료 
                정렬을 하게 되면 종료 시간(-1)이 시작 시간 보다 앞에 오게 되기 때문에 
                바로 회의를 시작할 수 있습니다.
             */
            meetings.Sort((a, b) => a.time == b.time ? a.type.CompareTo(b.type) : a.time.CompareTo(b.time));

            int MaxRooms = 0; // 필요한 최대 회의실 수
            int currentRooms = 0;  // 현재 사용 중인 회의실 수

            foreach (var meeting in meetings)
            {
                currentRooms += meeting.type; // 회의 시간이면 +1, 회의 시간이면 -1
                MaxRooms = Math.Max(MaxRooms, currentRooms); // 최대 회의실 수 갱신

            }
            // 출력하기
            Console.WriteLine(MaxRooms);
        }
    }
}
