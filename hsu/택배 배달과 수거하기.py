def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery = 0  # 배달 카운트
    pickup = 0  # 수거 카운트

    for i in range(n - 1, -1, -1):  # 뒤에서 부터 배달, 수거 함
        delivery += deliveries[i]  # 배달 카운트에 현재 집의 배달 갯수 더함
        pickup += pickups[i]  # 수거 카운트에 현재 집의 수거 갯수 더함

        while delivery > 0 or pickup > 0:
            delivery -= cap
            pickup -= cap
            answer += (i + 1) * 2  # 거리 계산

    return answer
