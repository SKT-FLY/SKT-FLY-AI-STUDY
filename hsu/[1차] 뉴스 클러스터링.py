def union(str1_list, str2_list):
    union_dict = {}

    for elem in str1_list:
        if elem in union_dict:
            union_dict[elem] += 1
        else:
            union_dict[elem] = 1

    for elem in str2_list:
        if elem in union_dict:
            union_dict[elem] = max(union_dict[elem], str2_list.count(elem))
        else:
            union_dict[elem] = str2_list.count(elem)

    union_len = sum(union_dict.values())
    return union_len


def intersection(str1_list, str2_list):
    intersection_dict = {}

    for elem in str1_list:
        if elem in intersection_dict:
            intersection_dict[elem] += 1
        else:
            intersection_dict[elem] = 1

    intersection_len = 0
    for elem in str2_list:
        if elem in intersection_dict and intersection_dict[elem] > 0:
            intersection_len += 1
            intersection_dict[elem] -= 1

    return intersection_len


def make_set(text):
    text = text.lower()
    str_list = []
    for i in range(len(text) - 1):
        if text[i : i + 2].isalpha():
            str_list.append(text[i : i + 2])
    return str_list


def solution(str1, str2):
    answer = 0

    str1_list = make_set(str1)
    str2_list = make_set(str2)

    print(str1_list, str2_list)

    union_len = union(str1_list, str2_list)
    intersection_len = intersection(str1_list, str2_list)

    if intersection_len == union_len:
        answer = 65536
    else:
        answer = int(intersection_len / union_len * 65536)

    return answer
