import java.util.*;

class Solution {
    
    public Set<Integer> made;
    
    public boolean[] isSelected;
    
    public boolean isPrime(int num) {
        if (num < 2) return false;
        
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        
        return true;
    }
    
    public void backtracking(int[] numbers, int current) {
        for (int i = 0; i < numbers.length; i++) {
            
            // 이미 선택한 수라면
            if (isSelected[i]) continue;
            
            // 선택
            int next = current * 10 + numbers[i];
            isSelected[i] = true;
            made.add(next);
            
            backtracking(numbers, next);
            
            // 선택 해제
            isSelected[i] = false;   
        }
    }
    
    public int solution(String numbers) {
        
        int[] nums = new int[numbers.length()];
        
        for (int i = 0; i < numbers.length(); i++) {
            nums[i] = numbers.charAt(i) - '0';
        }
        
        // 모든 순열 
        made = new HashSet<>();
        isSelected = new boolean[numbers.length()];
        
        backtracking(nums, 0);
        
        int answer = 0;
        
        for (int num: made) {
            if (isPrime(num)) answer++;
        }
        
        return answer;
    }
}