# 숫자 범위를 설정 무조건 오름차순으로 정리
# 오름차순으로정리된 숫자 중 k번째 숫자를 선택
import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())
array = list(map(int, input().strip().split()))

for _ in range(m):
    start, end, lo = map(int, input().strip().split())
    narry = array[start - 1 : end]
    narry.sort()
    print(narry[lo - 1])
