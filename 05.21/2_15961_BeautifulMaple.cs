using System;

class Solution
{
    public static int solution(int N, int d, int k, int c, int[] sushi)
    {
        // 1. k개의 접시를 연속으러 먹을 경우 할인된 정액 가격으로 제공
        // 초밥의 종류가 적힌 쿠폰 발행
        // 1번 행사에 참여할 경우 이 쿠폰에 적혀진 종류의 초밥 하나를 추가로 무료 제공

        // K = 4, 30번 쿠폰
        // 쿠폰을 고려하지 않을 경우 (9, 7, 30, 2), (30, 2, 7, 9), (2, 7, 9, 25)
        // 쿠폰을 사용시  (2, 7, 9, 25) + 30 최대 5가지

        int[] eat = new int[d + 1]; // 각 번호의 초밥을 먹은 횟수
        int total = 0;  // 현재 먹은 초밥의 종류 수
        int max = 0;    // 최대 먹을 수 있는 초밥의 종류 수


        // 초기 k개의 초밥 종류 수 계산
        for (int i = 0; i < k; i++)
        {
            if (eat[sushi[i]] == 0) total++;
            eat[sushi[i]]++;
        }
        max = total;

        // 찾아본 방법
        // 회전 초밥 돌아가기
        for (int i = 0; i < N; i++)
        {
            // 돌아가는 맨 앞의 회전 초밥을 빼고
            int removeIndex = i % N;
            if (eat[sushi[removeIndex]] == 1) total--;
            eat[sushi[removeIndex]]--;

            // 새 초밥을 추가
            // (0 + 4) % 10 = 3 => 0 1 2 3, 4
            // (8 + 4) % 10 = 1 => 8 9 0 1, 4 
            int newSushiIndex = (i + k) % N; // 원형으로 회전하기 때문에
            if (eat[sushi[newSushiIndex]] == 0) total++;
            eat[sushi[newSushiIndex]]++;

            // 쿠폰 초밥을 고려하여 최대값을 갱신
            if (eat[c] == 0)
            {
                // 쿠폰 초밥 한 개 사용
                max = Math.Max(max, total + 1);
            }
            else
            {
                max = Math.Max(max, total);
            }
        }
        return max;
    }
}

class Program
{
    static void Main(string[] args)
    {
        // N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
        string[] Input = Console.ReadLine().Split();
        int N = int.Parse(Input[0]);    // 접시의 수
        int d = int.Parse(Input[1]);    // 초밥의 가짓수
        int k = int.Parse(Input[2]);    // 연속해서 먹는 접시의 수
        int c = int.Parse(Input[3]);    // 쿠폰 번호

        // 회전하는 초밥 종류
        int[] sushi = new int[N];
        for (int i = 0; i < N; i++)
        {
            sushi[i] = int.Parse(Console.ReadLine());
        }

        Console.WriteLine(Solution.solution(N, d, k, c, sushi));
    }
}
