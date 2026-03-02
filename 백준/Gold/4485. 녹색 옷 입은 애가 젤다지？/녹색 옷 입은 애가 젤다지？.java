import java.io.*;
import java.util.*;

public class Main {

    static final int[][] directions = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };

    static int N, answer;
    static int[][] cave;
    static int[][] visited;

    static boolean isInside(int x, int y) {
        return 0 <= x && x < N && 0 <= y && y < N;
    }

    static void solution() {

        // 최소 힙 구조 (링크 비용 오름차순)
        Queue<int[]> pq = new PriorityQueue<>(
                (e1, e2) -> {
                    return Integer.compare(e1[0], e2[0]);
                }
        );
        pq.offer(new int[] { cave[0][0], 0, 0 });
        visited[0][0] = cave[0][0];

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int x  = cur[1];
            int y = cur[2];

            for (int i = 0; i < 4; i++) {
                int nx = x + directions[i][0];
                int ny = y + directions[i][1];

                if (!isInside(nx, ny)) continue;

                // 다음 좌표까지 드는 비용
                int nextCost = visited[x][y] + cave[nx][ny];

                // 다음 좌표까지 더 짧은 비용으로 갈 수 있다면
                if (visited[nx][ny] > nextCost) {
                    pq.offer(new int[] { cave[nx][ny], nx, ny });
                    visited[nx][ny] = nextCost;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        // 동굴의 크기
        N = Integer.parseInt(br.readLine());

        int tc = 1;

        while (N != 0) {
            answer  = Integer.MAX_VALUE;
            cave = new int[N][N];
            visited = new int[N][N];

            for (int[] row: visited) {
                Arrays.fill(row, Integer.MAX_VALUE);
            }

            // 동굴 내의 도둑 루피 정보 입력
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());

                for (int j = 0; j < N; j++) {
                    cave[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            // 최소 비용 탐색
            solution();

            answer = visited[N - 1][N - 1];

            sb.append("Problem ").append(tc++).append(": ").append(answer).append("\n");

            N = Integer.parseInt(br.readLine());
        }

        System.out.println(sb);
    }
}
