import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
nlist = [i + 1  for i in range(n)]
answer = []
while len(nlist) != 0:
    if k > len(nlist):
        if type(nlist) is not deque:
            nlist = deque(nlist)
        for _ in range(k - 1):
            nlist.append(nlist.popleft())
        answer.append(nlist.popleft())
    else:
        front = nlist[:k - 1]
        back = nlist[k:]
        target = nlist.pop(k - 1)
        nlist = back + front
        answer.append(target)
print("<" + ", ".join(list(map(str, answer))) + ">")
