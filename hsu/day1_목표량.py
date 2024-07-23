# from itertools import permutations

# n_list = list("".join(input()))
# 타겟값 생성
# target = tuple(n_list)
# n = len(n_list)

# # print(n_list)
# 순열 확인 경우의 수 다 체크
# combi = list(permutations(n_list, n))

# 경우의 수 다 확인 후 크기순 정렬
# n_list = sorted(combi, key = lambda x : "".join(x))
# # print(n_list)
# # print(n_list.index(target))
# 타겟값 다음값 정답
# print("".join(n_list[n_list.index(target) + 1]))
########
# 전체 케이스 확인 후 정렬하려고 했지만, permutations 함수 자체에 시간복잡도가 높아 시간초과로 예상됨


def permutations(target):
    num_list = list(target)

    n = len(num_list)

    # 리스트 마지막 값 2개 확인
    i = n - 2

    # 값이 바뀌 앞부분 보다 커지는 지점 확인(감소하는 지점)
    while i >= 0 and num_list[i] >= num_list[i + 1]:
        i -= 1

    # 다음 큰 값을 위한 변수
    j = n - 1

    # 다음 큰 값 확인
    while num_list[i] >= num_list[j]:
        j -= 1

    # 감소하는 지점과 다음 큰 값 위치 변경
    num_list[i], num_list[j] = num_list[j], num_list[i]

    # 리스트 정돈
    num_list = num_list[: i + 1] + sorted(num_list[i + 1 :])

    return "".join(num_list)


n_list = list("".join(input()))
target = "".join(n_list)
print(permutations(target))
