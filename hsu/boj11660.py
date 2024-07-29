import sys


n, m = map(int, sys.stdin.readline().split())

map_list = []

for _ in range(n):
    map_list.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            dp[i][j] = map_list[i][j]
        elif j == 0:
            dp[i][j] = dp[i - 1][j] + map_list[i][j]
        elif i == 0:
            dp[i][j] = dp[i][j - 1] + map_list[i][j]
        else:
            dp[i][j] = dp[i][j - 1] + map_list[i][j] + dp[i - 1][j] - dp[i - 1][j - 1]

# for i in dp:
#     print(i)


for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1

    answer = dp[x2][y2]
    if x1 == x2 and y1 == y2:
        answer = map_list[x1][y1]
    elif x1 > 0 and y1 > 0:
        answer += dp[x1 - 1][y1 - 1] - dp[x1 - 1][y2] - dp[x2][y1 - 1]
    elif y1 > 0:
        answer -= dp[x2][y1 - 1]
    elif x1 > 0:
        answer -= dp[x1 - 1][y2]

    print(answer)
