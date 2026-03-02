import java.io.*;
import java.util.*;

public class Main {

    static class Node {
        int importance;
        boolean isTarget;

        public Node(int importance, boolean isTarget) {
            this.importance = importance;
            this.isTarget = isTarget;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int target = Integer.parseInt(st.nextToken());

            // 실제 순서를 유지하는 큐
            Deque<Node> q = new ArrayDeque<>();
            PriorityQueue<Integer> maxPQ = new PriorityQueue<>(Collections.reverseOrder());

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                int imp = Integer.parseInt(st.nextToken());
                boolean isTarget = (i == target);
                q.offerLast(new Node(imp, isTarget));
                maxPQ.offer(imp);
            }

            int printSeq = 0;

            while (!q.isEmpty()) {
                Node cur = q.pollFirst();

                // 현재 큐 전체에서 가장 큰 중요도
                int curMax = maxPQ.peek();

                // 맨 앞 문서의 중요도가 최댓값보다 작으면 뒤로 보냄
                if (cur.importance < curMax) {
                    q.offerLast(cur);
                    continue;
                }
                
                printSeq++;
                maxPQ.poll();

                if (cur.isTarget) {
                    sb.append(printSeq).append("\n");
                    break;
                }
            }
        }

        System.out.print(sb);
    }
}