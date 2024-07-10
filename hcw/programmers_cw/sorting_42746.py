def solution(numbers):
    # 숫자들을 문자열로 변환
    str_numbers = list(map(str, numbers))
    # 4번 반복한 문자열을 기준으로 비교해서 sort 적용
    # e.g. [1, 10, 12] -> 1111, 10101010, 12121212
    str_numbers.sort(key=lambda x: x*4, reverse=True)
    # numbers의 원소가 모두 0인 경우 단순 '0'만 반환해야 함
    if str_numbers[0] == '0':
        return '0'
    # join 시켜 하나의 문자열로 반환
    return ''.join(str_numbers)