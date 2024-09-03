from collections import deque

n = int(input())
pop_list = list(map(int, input().split()))

balloon = deque([x for x in range(1, n + 1)])

answer = []
# print(balloon)
answer.append(balloon.popleft())
cur_index = pop_list[0]
while balloon:
    # print(cur_index)
    if cur_index > 0:
        for _ in range(cur_index - 1):
            # print(balloon)
            balloon.append(balloon.popleft())
    else:
        for _ in range(abs(cur_index)):
            # print(balloon)
            balloon.appendleft(balloon.pop())
            # print(balloon)
    p = balloon.popleft()
    # print(p)
    answer.append(p)
    cur_index = pop_list[p - 1]


for i in answer:
    print(i, end=" ")
