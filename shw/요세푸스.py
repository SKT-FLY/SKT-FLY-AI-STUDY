from collections import deque

def josephus(N, K):

    people = deque(range(1, N+1))
    pop_list =[]

    while people:
        people.rotate(-(K-1)) # 오른쪽으로 이동하려면 왼쪽으로 rotate해야함 (본인의 현재위치를 고려해야함 --> 풍선터뜨리기 문제에서도!)
        pop_list.append(people.popleft())

    return pop_list

N = int(input("사람의 수 입력: "))
K = int(input("제거할 순서 입력: "))

result = josephus(N, K)
print("요세푸스 문제:", result)