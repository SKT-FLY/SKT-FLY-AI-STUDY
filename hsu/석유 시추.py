from collections import deque


def bfs(x, y, land, visited, n, m, chunk_id):
    queue = deque([(x, y)])
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    area_size = 0

    while queue:
        cx, cy = queue.popleft()
        area_size += 1
        land[cx][cy] = chunk_id  # 덩어리 ID로 마킹

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if (
                0 <= nx < n
                and 0 <= ny < m
                and not visited[nx][ny]
                and land[nx][ny] == 1
            ):
                visited[nx][ny] = True
                queue.append((nx, ny))

    return area_size


def solution(land):
    n = len(land)
    m = len(land[0])
    visited = [[False] * m for _ in range(n)]
    chunk_sizes = {}
    chunk_id = 2  # 덩어리 ID는 2부터 시작 (0과 1을 피하기 위해)

    # 각 연결된 석유 덩어리를 찾고 크기를 기록
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                size = bfs(i, j, land, visited, n, m, chunk_id)
                chunk_sizes[chunk_id] = size
                chunk_id += 1

    # 모든 열에서 최대 석유량을 계산
    max_oil = 0
    for j in range(m):
        column_oil = 0
        seen_chunks = set()
        for i in range(n):
            if land[i][j] > 1 and land[i][j] not in seen_chunks:
                chunk_id = land[i][j]
                column_oil += chunk_sizes[chunk_id]
                seen_chunks.add(chunk_id)
        max_oil = max(max_oil, column_oil)

    return max_oil
