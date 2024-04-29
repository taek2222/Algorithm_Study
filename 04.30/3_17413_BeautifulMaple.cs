// 백준 17413
//https://www.acmicpc.net/problem/17413

/*
 문자열 S는 아래와 같은 규칙을 지킨다
1. 알파벳 소문자('a'-'z'), 숫자('0'-'9'), 공백(' '), 
    특수 문자('<', '>')로만 이루어져 있다.
2. 문자열의 시작과 끝은 공백이 아니다.
3. '<'와 '>'가 문자열에 있는 경우 번갈아가면서 등장하며, '<'이 먼저 등장한다. 또, 두 문자의 개수는 같다.
Ex) <ab cd>ef gh<ij kl>
    <ab cd>fe hg<ij kl>
    
<순서 안 바뀌지롱> 나는 순서가 바뀌지롱
코드는 다른 코드를 참조해서 작성
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Baekjoon
{
    class Program
    {
        static void Main(string[] args)
        {
            string S = Console.ReadLine();
            // 새 객체를 만들지 않고 데이터를 재사용하고 수정할 수 있음
            StringBuilder result = new StringBuilder();
            Stack<char> stack = new Stack<char>();
            bool Tag = false;

            foreach (char c in S)
            {
                if(c == '<')
                {
                    while(stack.Count > 0) result.Append(stack.Pop());
                    Tag = true; // 태그 안으로 진입
                    result.Append(c);
                }
                else if (c == '>')
                {
                    Tag = false;    // 태그 밖으로 나옴
                    result.Append(c);
                }
                else if (Tag)
                {
                    // 태그 안의 문자는 그대로 결과 문자열에 추가
                    result.Append(c);
                }
                else
                {
                    if(c == ' ')
                    {
                        // 공백 문자를 만나면 스택에 쌓인 문자들을 결과 문자에 추가하기
                        while(stack.Count > 0) { result.Append(stack.Pop());}
                        result.Append(c); //
                    }
                    else
                    {
                        stack.Push(c);
                    }
                }
            }
            // 마지막으로 스택에 남아 있는 문자들을 결과 문자열에 추가
            while(stack.Count > 0) result.Append(stack.Pop());
            Console.WriteLine(result.ToString());
        }
    }
}
