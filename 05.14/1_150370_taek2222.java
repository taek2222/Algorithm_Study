/*
    https://school.programmers.co.kr/learn/courses/30/lessons/150370

    고객의 약관 동의를 얻어서 수집된 1~n번으로 분류되는 개인정보 n개가 있습니다.
    약관 종류는 여러 가지 있으며 각 약관마다 개인정보 보관 유효기간이 정해져 있습니다.
    당신은 각 개인정보가 어떤 약관으로 수집됐는지 알고 있습니다.
    수집된 개인정보는 유효기간 전까지만 보관 가능하며, 유효기간이 지났다면 반드시 파기해야 합니다.

    예를 들어, A라는 약관의 유효기간이 12 달이고,
    2021년 1월 5일에 수집된 개인정보가 A약관으로 수집되었다면
    해당 개인정보는 2022년 1월 4일까지 보관 가능하며
    2022년 1월 5일부터 파기해야 할 개인정보입니다.

    당신은 오늘 날짜로 파기해야 할 개인정보 번호들을 구하려 합니다.

    모든 달은 28일까지 있다고 가정합니다.

    다음은 오늘 날짜가 2022.05.19일 때의 예시입니다.

    약관 종류	유효기간
    A	6 달
    B	12 달
    C	3 달

    번호	개인정보 수집 일자	약관 종류
    1	 2021.05.02	     A
    2	 2021.07.01	     B
    3	 2022.02.19	     C
    4	 2022.02.20	     C

    첫 번째 개인정보는 A약관에 의해 2021년 11월 1일까지 보관 가능하며, 유효기간이 지났으므로 파기해야 할 개인정보입니다.
    두 번째 개인정보는 B약관에 의해 2022년 6월 28일까지 보관 가능하며, 유효기간이 지나지 않았으므로 아직 보관 가능합니다.
    세 번째 개인정보는 C약관에 의해 2022년 5월 18일까지 보관 가능하며, 유효기간이 지났으므로 파기해야 할 개인정보입니다.
    네 번째 개인정보는 C약관에 의해 2022년 5월 19일까지 보관 가능하며, 유효기간이 지나지 않았으므로 아직 보관 가능합니다.
    따라서 파기해야 할 개인정보 번호는 [1, 3]입니다.

    오늘 날짜를 의미하는 문자열 today,
    약관의 유효기간을 담은 1차원 문자열 배열 terms와
    수집된 개인정보의 정보를 담은 1차원 문자열 배열 privacies가 매개변수로 주어집니다.

    이때 파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

    today	        terms	                privacies	                                                                        result
    "2022.05.19"	["A 6", "B 12", "C 3"]	["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]	                [1, 3]
    "2020.01.01"	["Z 3", "D 5"]	        ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]	[1, 4, 5]
*/

import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        String today = "2022.05.19";
        String[] terms = {"A 6", "B 12", "C 3"};
        String[] privacies = {"2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"};

        System.out.println(Arrays.toString(solution(today, terms, privacies)));
    }

    public static int[] solution(String today, String[] terms, String[] privacies) {
        List<Integer> list = new ArrayList<>();
        Map<String, Integer> map = new HashMap<>();

        // 약관 종류와 기간(개월)을 map에 저장
        for (String term : terms) {
            String[] parts = term.split(" ");
            map.put(parts[0], Integer.parseInt(parts[1]));
        }

        // 오늘 날짜를 파싱
        String[] todayParts = today.split("\\.");
        int todayYear = Integer.parseInt(todayParts[0]);
        int todayMonth = Integer.parseInt(todayParts[1]);
        int todayDay = Integer.parseInt(todayParts[2]);

        // 오늘 날짜를 일수로 변환
        int todayInDays = toDays(todayYear, todayMonth, todayDay);

        // 각 개인정보 항목을 확인
        for (int i = 0; i < privacies.length; i++) {
            String[] privacyParts = privacies[i].split(" ");
            String[] dateParts = privacyParts[0].split("\\.");
            int privacyYear = Integer.parseInt(dateParts[0]);
            int privacyMonth = Integer.parseInt(dateParts[1]);
            int privacyDay = Integer.parseInt(dateParts[2]);
            int termDurationInMonths = map.get(privacyParts[1]);

            // 개인정보 날짜를 일수로 변환하고 약관 기간을 더함
            int privacyInDays = toDays(privacyYear, privacyMonth, privacyDay);
            int expiryInDays = privacyInDays + termDurationInMonths * 28;

            // 만료일이 오늘 날짜 이전이거나 같은 경우 리스트에 추가
            if (expiryInDays <= todayInDays) {
                list.add(i + 1);
            }
        }

        // 리스트를 배열로 변환하여 반환
        return list.stream().mapToInt(Integer::intValue).toArray();
    }

    // 날짜를 연도 0부터의 총 일수로 변환 (비교를 위해)
    private static int toDays(int year, int month, int day) {
        return year * 12 * 28 + month * 28 + day;
    }
}
