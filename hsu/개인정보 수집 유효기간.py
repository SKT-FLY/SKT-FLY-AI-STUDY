def solution(today, terms, privacies):
    answer = []
    today = int(today[:4]) * 12 * 28 + int(today[5:7]) * 28 + int(today[-2:])
    # print(today)
    day_dict = {}
    for d in terms:
        term, day = d.split()
        day_dict[term] = int(day) * 28

    # print(day_dict)
    for i, days in enumerate(privacies):
        day, term = days.split()
        day = (
            int(day[:4]) * 12 * 28 + int(day[5:7]) * 28 + int(day[-2:]) + day_dict[term]
        )
        # print(day)
        if day <= today:
            answer.append(i + 1)

    return answer
