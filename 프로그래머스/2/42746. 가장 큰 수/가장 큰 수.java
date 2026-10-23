import java.util.*;

class Solution {
    
    public String solution(int[] numbers) {
        
        String[] values = new String[numbers.length];

        for (int i = 0; i < numbers.length; i++) {
            values[i] = Integer.toString(numbers[i]);
        }

        // 두 수를 붙인 결과가 더 큰 순서로 정렬
        Arrays.sort(values, (a, b) -> (b + a).compareTo(a + b));

        // 가장 앞이 0이면 모든 원소가 0
        if (values[0].equals("0")) {
            return "0";
        }

        StringBuilder answer = new StringBuilder();

        for (String value : values) {
            answer.append(value);
        }

        return answer.toString();
    }
}