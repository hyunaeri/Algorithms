import java.util.*;

class Solution {
    
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int processed = 0;
        
        for (int[] command: commands) {
            
            int start = command[0] - 1;
            int end = command[1] - 1;
            int target = command[2] - 1;
            
            int[] temp = new int[end - start + 1];
            int idx = 0;
            
            while (start <= end) {
                temp[idx++] = array[start++];
            }
            
            // 오름차순 정렬
            Arrays.sort(temp);
            
            answer[processed++] = temp[target];
        }
        
        return answer;
    }
}