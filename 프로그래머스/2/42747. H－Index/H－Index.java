import java.util.*;

class Solution {
    
    public int solution(int[] citations) {
        
        // 오름차순 정렬
        Arrays.sort(citations);
        
        for (int i = 0; i < citations.length; i++) {
            
            // h는 논문 개수를 넘을 수 없다.
            int h = citations.length - i;
            
            if (citations[i] >= h) {
                return h;
            }

        }
        
        return 0;
    }
}