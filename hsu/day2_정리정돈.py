n, m = map(int, input().split())

n_list = list(map(int, input().split()))

for _ in range(m):
    s, e, k = list(map(int, input().split()))
    print(sorted(n_list[s - 1 : e])[k - 1])
