import java.io.*;
import java.util.*;

public class Main {

    static final int[][] directions = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };

    static int N, answer;
    static int[][] cave;
    static int[][] dist;

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
        dist[0][0] = cave[0][0];
        pq.offer(new int[] { dist[0][0], 0, 0 });

        while (!pq.isEmpty()) {

            // 우선 순위 큐에서 꺼낸 노드는 해당 노드까지의 최단 거리가 확정된 상태
            int[] cur = pq.poll();
            int cost = cur[0];
            int x  = cur[1];
            int y = cur[2];

            // 우선 순위 큐에 같은 좌표가 여러 번 들어올 수 있는데, 이미 더 좋은 거리로 갱신 됐다면 무시
            if (cost != dist[x][y]) continue;

            if (x == N - 1 && y == N - 1) {
                answer = cost;
                return;
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + directions[i][0];
                int ny = y + directions[i][1];

                if (!isInside(nx, ny)) continue;

                // 다음 좌표까지 드는 비용
                int nextCost = cost + cave[nx][ny];

                // 다음 좌표까지 더 짧은 비용으로 갈 수 있다면
                if (dist[nx][ny] > nextCost) {
                    dist[nx][ny] = nextCost;
                    pq.offer(new int[] { nextCost, nx, ny });
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
            dist = new int[N][N];

            for (int[] row: dist) {
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

            sb.append("Problem ").append(tc++).append(": ").append(answer).append("\n");

            N = Integer.parseInt(br.readLine());
        }

        System.out.println(sb);
    }
}