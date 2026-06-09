import java.util.*;

class Solution {

    public boolean solution(String[] phone_book) {
    
        // 전화번호 정렬
        Arrays.sort(phone_book);

        // 접두어 관계에 있는 전화번호들은 정렬 시 서로 붙어 있다.
        for (int i = 0; i < phone_book.length - 1; i++) {
            
            if (phone_book[i + 1].startsWith(phone_book[i])) {
                return false;
            }
        }

        return true;
    }
}