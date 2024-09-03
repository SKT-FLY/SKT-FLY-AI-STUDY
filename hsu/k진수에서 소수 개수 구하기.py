from collections import deque
import math


def baseConversion(n, k):
    num_deque = deque()
    if k == 10:
        return deque(str(n))
    else:
        while n > k:
            num_deque.appendleft(str(n % k))
            n = n // k

        num_deque.appendleft(str(n % k))
    return num_deque


def check_prime(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1


def solution(n, k):
    answer = 0
    # print(baseConversion(n, k))
    q = baseConversion(n, k)
    str_num = ""
    while q:
        n = q.popleft()
        if n == "0" and str_num:
            print(str_num)
            answer += check_prime(int(str_num))
            str_num = ""
        else:
            str_num += n
    answer += check_prime(int(str_num))
    return answer
