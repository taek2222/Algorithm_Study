import java.util.Arrays;

/*
    https://school.programmers.co.kr/learn/courses/30/lessons/258712

    - 문제 설명
    선물을 직접 전하기 힘들 때 카카오톡 선물하기 기능을 이용해 축하 선물을 보낼 수 있습니다.
    당신의 친구들이 이번 달까지 선물을 주고받은 기록을 바탕으로 다음 달에 누가 선물을 많이 받을지 예측하려고 합니다.

    두 사람이 선물을 주고받은 기록이 있다면,
    이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받습니다.

    예를 들어 A가 B에게 선물을 5번 줬고,
    B가 A에게 선물을 3번 줬다면
    다음 달엔 A가 B에게 선물을 하나 받습니다.

    두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면,
    선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받습니다.
    선물 지수는 이번 달까지 자신이 친구들에게 준 선물의 수에서 받은 선물의 수를 뺀 값입니다.

    예를 들어 A가 친구들에게 준 선물이 3개고 받은 선물이 10개라면 A의 선물 지수는 -7입니다.
    B가 친구들에게 준 선물이 3개고 받은 선물이 2개라면 B의 선물 지수는 1입니다.

    만약 A와 B가 선물을 주고받은 적이 없거나 정확히 같은 수로 선물을 주고받았다면,
    다음 달엔 B가 A에게 선물을 하나 받습니다.
    만약 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 않습니다.

    위에서 설명한 규칙대로 다음 달에 선물을 주고받을 때, 당신은 선물을 가장 많이 받을 친구가 받을 선물의 수를 알고 싶습니다.

    친구들의 이름을 담은 1차원 문자열 배열 friends
    이번 달까지 친구들이 주고받은 선물 기록을 담은 1차원 문자열 배열 gifts가 매개변수로 주어집니다.
    이때, 다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수를 return 하도록 solution 함수를 완성해 주세요.

    - 제한 사항
    2 ≤ friends의 길이 = 친구들의 수 ≤ 50
    friends의 원소는 친구의 이름을 의미하는 알파벳 소문자로 이루어진 길이가 10 이하인 문자열입니다.
    이름이 같은 친구는 없습니다.

    1 ≤ gifts의 길이 ≤ 10,000
    gifts의 원소는 "A B"형태의 문자열입니다.
    A는 선물을 준 친구의 이름을 B는 선물을 받은 친구의 이름을 의미하며 공백 하나로 구분됩니다.
    A와 B는 friends의 원소이며 A와 B가 같은 이름인 경우는 존재하지 않습니다.
*/

public class Solution {
    public static void main(String[] args) {
        String[] friends = {"muzi", "ryan", "frodo", "neo"};
        String[] gifts = {"muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"};

        System.out.println(solution(friends, gifts));
    }

    public static int solution(String[] friends, String[] gifts) {

        int arrayLength = friends.length;
        // 주고받은 선물 배열
        int[][] giftList = new int[arrayLength][arrayLength];
        // 선물 지수 배열 [ 열 (0 : 준 선물) (1 : 받은 선물) (2 : 선물 지수)
        int[][] index = new int[arrayLength][3];

        // 사전순으로 정렬
        Arrays.sort(friends);
        Arrays.sort(gifts);

        // 주고받은 선물 배열 값 삽입
        for(int i = 0, j = 0; i < arrayLength; i++) {
            for(; j < gifts.length; j++) {
                // 선물 기록 분할
                String[] name = gifts[j].split(" ");

                // 선물 주는 사람이 아닐 경우
                if(!name[0].equals(friends[i]))
                    break;

                // 선물 배열 카운팅
                giftList[i][Arrays.binarySearch(friends, name[1])]++;
            }
        }

        // 선물 지수 배열 값 삽입
        for(int i = 0; i < arrayLength; i++) {
            for (int j = 0; j < arrayLength; j++) {
                if (giftList[i][j] == 0)
                    continue;
                // 준 선물 카운팅
                index[i][0] += giftList[i][j];
                // 받은 선물 카운팅
                index[j][1] += giftList[i][j];
            }
        }

        // 선물 지수 값 계산
        for(int i = 0; i < arrayLength; i++)
            index[i][2] = index[i][0] - index[i][1];

        // 가장 많은 선물 값
        int maxGift = 0;
        for(int i = 0; i < arrayLength; i++) {
            int giftCount = 0;
            for(int j = 0; j < arrayLength; j++) {
                if (giftList[i][j] > giftList[j][i])
                    giftCount++;
                else if(giftList[i][j] == giftList[j][i]) {
                    if(index[i][2] > index[j][2])
                        giftCount++;
                }
            }
            if(giftCount > maxGift)
                maxGift = giftCount;
        }

        /*
        // 테스트 출력문
        System.out.println(Arrays.toString(friends));
        System.out.println(Arrays.toString(gifts));

        for(int i = 0; i < arrayLength; i++) {
            for (int j = 0; j < arrayLength; j++)
                System.out.print(giftList[i][j]);
            System.out.println();
        }

        for(int i = 0; i < arrayLength; i++) {
            for (int j = 0; j < 3; j++)
                System.out.print(index[i][j]);
            System.out.println();
        }
        */

        return maxGift;
    }
}
