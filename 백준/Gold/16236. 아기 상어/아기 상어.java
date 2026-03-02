import java.io.*;
import java.util.*;

public class Main {

	// 상하좌우
	static final int[][] directions = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };

	// 공간
	static int[][] space;
	static boolean[][] visited;

	// 아기 상어 크기, 먹은 물고기 카운터
	static int babySharkSize = 2;
	static int counter = 0;

	// 아기 상어의 좌표
	static int babySharkPosX;
	static int babySharkPosY;

	// 먹을 수 있는 물고기 반환 (BFS)
	static List<int[]> findEdibleFish() {
		List<int[]> result = new ArrayList<>();

		Queue<int[]> q = new ArrayDeque<>();
		q.offer(new int[] { babySharkPosX, babySharkPosY, 0 });
		visited[babySharkPosX][babySharkPosY] = true;

		while (!q.isEmpty()) {
			int[] current = q.poll();
			int cx = current[0], cy = current[1], dist = current[2];

			for (int[] dir : directions) {
				int nx = cx + dir[0];
				int ny = cy + dir[1];

				// 범위를 벗어나지 않는 선에서
				if (0 <= nx && nx < space.length && 0 <= ny && ny < space[0].length) {
					// 미 방문 지역이면서, 지나갈 수 있는 칸인지?
					if (!visited[nx][ny] && babySharkSize >= space[nx][ny]) {
						// 먹을 수 있는가?
						if (space[nx][ny] != 0 && babySharkSize > space[nx][ny]) {
							result.add(new int[] { nx, ny, dist + 1 });
						}
						visited[nx][ny] = true;
						q.offer(new int[] { nx, ny, dist + 1 });
					}
				}
			}
		}
		return result;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		// N * N 크기의 공간
		int N = Integer.parseInt(br.readLine());

		space = new int[N][N];
		visited = new boolean[N][N];

		// 공간 입력
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());

			for (int j = 0; j < N; j++) {
				int value = Integer.parseInt(st.nextToken());

				// 아기 상어 초기 좌표 미리 저장 후 빈 칸으로 간주
				if (value == 9) {
					babySharkPosX = i;
					babySharkPosY = j;
					value = 0;
				}

				space[i][j] = value;
			}
		}

		// 정답
		int answer = 0;

		while (true) {
			// 매번 초기화
			visited = new boolean[N][N];

			// 먹을 수 있는 물고기 리스트 반환
			List<int[]> fishList = findEdibleFish();

			// 더 이상 먹을 물고기가 없는 경우
			if (fishList.isEmpty())
				break;

			else {
				// 우선순위에 맞게 정렬 (거리, 행, 열)
				Collections.sort(fishList, (a, b) -> {
					if (a[2] != b[2]) return a[2] - b[2];
					if (a[0] != b[0]) return a[0] - b[0];
					return a[1] - b[1];
				});

				int[] target = fishList.get(0);
				int targetX = target[0], targetY = target[1], targetDistance = target[2];

				// 이동 시간 누적
				answer += targetDistance;

				// 먹기
				space[targetX][targetY] = 0;

				// 상어 위치 갱신
				babySharkPosX = targetX;
				babySharkPosY = targetY;

				// 물고기 카운터 증가
				counter++;

				// 사이즈 업
				if (babySharkSize == counter) {
					babySharkSize++;
					counter = 0;
				}
			}
		}
		System.out.println(answer);
	}
}
