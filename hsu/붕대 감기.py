def solution(bandage, health, attacks):
    max_health = health
    t, x, y = bandage
    current_time = 0

    for attack_time, damage in attacks:
        # 공격 전까지 남은 시간을 계산
        time_diff = attack_time - current_time - 1

        if time_diff > 0:
            # 연속적으로 성공할 수 있는 횟수
            full_successes = time_diff // t
            remaining_time = time_diff % t

            # 전체 회복량 계산
            health += full_successes * (t * x + y)
            health += remaining_time * x

            # 최대 체력을 초과하지 않도록 제한
            health = min(health, max_health)

        # 공격을 받음
        health -= damage

        if health <= 0:
            return -1

        current_time = attack_time

    # 공격 이후 남은 시간 동안 붕대 감기 사용
    if current_time < attacks[-1][0]:
        remaining_time = attacks[-1][0] - current_time
        health += remaining_time * x
        health = min(health, max_health)

    return health
