import java.io.*;
import java.util.*;

public class Main {

    static int longestDist = Integer.MIN_VALUE;
    static int goldenEdges = 0;

    static int n, m, src, dst;

    static List<List<int[]>> graph;
    static List<List<int[]>> reversedGraph;
    static int[] indegree;
    static int[] maxDistance;

    static void solution() {
        Queue<Integer> q = new ArrayDeque<>();

        maxDistance[src] = 0;

        // 현재 정점
        q.offer(src);

        while (!q.isEmpty()) {
            int city = q.poll();

            for (int[] nextInfo: graph.get(city)) {
                int nextCity = nextInfo[0];
                int nextDist = nextInfo[1];

                // city 가 src 에서 도달 가능한 경우에만
                if (maxDistance[city] != -1) {
                    maxDistance[nextCity] = Math.max(maxDistance[nextCity], maxDistance[city] + nextDist);
                }

                // 다음 도시 진입 차수 1 감소
                indegree[nextCity]--;

                // 진입 차수가 0 인 도시를 큐에 삽입
                if (indegree[nextCity] == 0) {
                    q.offer(nextCity);
                }
            }
        }

        longestDist = maxDistance[dst];
    }

    static void countEdges() {
        boolean[] visited = new boolean[n + 1];
        Queue<Integer> q = new ArrayDeque<>();

        q.offer(dst);
        visited[dst] = true;

        int count = 0;

        while (!q.isEmpty()) {
            int city = q.poll();

            for (int[] prevInfo: reversedGraph.get(city)) {
                int prevCity = prevInfo[0];
                int prevDist = prevInfo[1];

                // prev 가 src 에서 도달 불가면 생략
                if (maxDistance[prevCity] == -1) continue;

                // 최대 시간이 걸리는 경로가 맞는지 체크
                if (maxDistance[prevCity] + prevDist == maxDistance[city]) {
                    count++;

                    if (!visited[prevCity]) {
                        visited[prevCity] = true;
                        q.offer(prevCity);
                    }
                }
            }
        }
        goldenEdges = count;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 도시의 개수
        n = Integer.parseInt(br.readLine());
        graph = new ArrayList<>();
        reversedGraph = new ArrayList<>();
        indegree = new int[n + 1];
        maxDistance = new int[n + 1];

        // -1 이면 도달 불가 상태
        Arrays.fill(maxDistance, -1);

        for (int i = 0; i <= n ; i++) {
            graph.add(new ArrayList<>());
            reversedGraph.add(new ArrayList<>());
        }

        // 도로의 개수
        m = Integer.parseInt(br.readLine());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            graph.get(start).add(new int[] {end, cost});
            reversedGraph.get(end).add(new int[] {start, cost});
            indegree[end]++;
        }

        // 한걸음과 로마 번호
        st = new StringTokenizer(br.readLine());
        src = Integer.parseInt(st.nextToken());
        dst = Integer.parseInt(st.nextToken());

        solution();
        countEdges();

        System.out.println(longestDist);
        System.out.println(goldenEdges);
    }
}
