import sys

input = sys.stdin.readline
n, m = map(int, input().strip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = graph[0][0]
for i in range(n):
    for j in range(n):
        if i > 0 and j > 0:
            dp[i][j] = graph[i][j] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
        elif i == 0:
            dp[i][j] = graph[i][j] + dp[i][j - 1]
        elif j == 0:
            dp[i][j] = graph[i][j] + dp[i - 1][j]
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().strip().split())
    x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
    if x1 > 0 and y1 > 0:
        answer = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    elif x1 == x2 and y1 == y2 :
        answer = graph[x1][y1]
    elif x1 == 0 and y1 != 0:
        answer = dp[x2][y2] - dp[x2][y1 - 1]
    elif x1 != 0 and y1 == 0:
        answer = dp[x2][y2] - dp[x1 - 1][y2]
    else:
        answer = dp[x2][y2]
    print(answer)

