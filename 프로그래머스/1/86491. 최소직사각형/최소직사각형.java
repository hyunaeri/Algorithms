class Solution {
    public int solution(int[][] sizes) {
        
        int maxShortSide = 0;
        int maxLongSide = 0;

        for (int[] size : sizes) {
            int shortSide = Math.min(size[0], size[1]);
            int longSide = Math.max(size[0], size[1]);

            maxShortSide = Math.max(maxShortSide, shortSide);
            maxLongSide = Math.max(maxLongSide, longSide);
        }

        return maxShortSide * maxLongSide;
    }
}