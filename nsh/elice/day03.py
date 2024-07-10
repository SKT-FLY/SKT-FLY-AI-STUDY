import sys
from collections import deque

input = sys.stdin.readline

ilist = list(input().strip())
ilist = ilist[::-1]
stack = deque([])
i = 0
while True:
    if i == len(ilist):
        break
    if ilist[i] == ")":
        stack.append(i)  # 인덱스를 삽입
    elif ilist[i] == "(":
        start = stack.pop()
        target = ilist[start + 1 : i]
        nlist = ilist[:start] + (target * int(ilist[i + 1]))
        if i + 2 < (len(ilist)):
            ilist = nlist + ilist[i + 2 :]
        else:
            ilist = nlist
        i = len(nlist)
        continue
    i += 1
print(len(ilist))
