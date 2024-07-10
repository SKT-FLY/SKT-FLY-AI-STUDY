n = 364

str_n_list = list(str(n))
len_n = len(str(n))

switched = 0
for i in range (len_n-1, 0, -1):
    for k in range (len_n-2, -1, -1):
        if str_n_list[i] > str_n_list[k]:
            str_n_list[i], str_n_list[k] = str_n_list[k], str_n_list[i]
            switched = 1
            break
    if switched == 1:
        break
str_n_list = str_n_list[:k + 1] + sorted(str_n_list[k + 1:])

answer = int(''.join(str_n_list))
print(answer)  # 436이 출력되어야 함