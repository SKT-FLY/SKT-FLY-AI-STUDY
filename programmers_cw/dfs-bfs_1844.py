from collections import deque

def solution(maps):
    n, m = len(maps[0]), len(maps)  # 목표 지점 (열, 행)
    loc_deque = deque([((1, 1), [(1, 1)])])  # 시작 지점으로 덱 초기화

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우 이동방향
    visited = {(1, 1)}  # 방문 지점 저장

    while loc_deque:  # deque가 비어 있지 않은 동안
        (loc_now, path) = loc_deque.popleft()
        (row_now, col_now) = loc_now  # (행, 열)

        for direc in directions:
            row_next, col_next = row_now + direc[0], col_now + direc[1]
            if 1 <= row_next <= m and 1 <= col_next <= n and maps[row_next - 1][
                col_next - 1] == 1:  # 다음 지점이 맵 내이고, 이동 가능(1)한 지점인 경우
                if (row_next, col_next) not in visited:
                    visited.add((row_next, col_next))
                    loc_deque.append(((row_next, col_next), path + [(row_next, col_next)]))
                    if (row_next, col_next) == (m, n):
                        return len(path) + 1

    return -1  # 목표 지점에 도착할 수 없는 경우