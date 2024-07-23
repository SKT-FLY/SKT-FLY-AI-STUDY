from collections import deque

n, k = map(int, input().split())

josephus = deque([x for x in range(1, n + 1)])

answer = []

while josephus:
    for _ in range(k - 1):
        # K - 1 갯수만큼 뒤로 미루기
        josephus.append(josephus.popleft())
    answer.append(josephus.popleft())

# 출력 형식을 맞추기 위한 코드
print("<", end="")

for x in answer[:-1]:

    print(x, end=", ")

print(str(answer[-1]) + ">")
