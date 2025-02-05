lst_count = int(input())

full_list = []
max_n = 0
for i in range(lst_count):
    if (n := int(input())) > max_n:
        max_n = n
    full_list.append(list(map(int, input().split())))


def merge(lst1, lst2):

    sort_list = []
    i, j = 0, 0

    while i < len(lst1) and j < len(lst2):

        if lst1[i] < lst2[j]:
            sort_list.append(lst1[i])
            i += 1
        else:
            sort_list.append(lst2[j])
            j += 1

    sort_list.extend(lst1[i:])
    sort_list.extend(lst2[j:])

    return sort_list


def merge_n_list(list_collection):
    if len(list_collection) == 1:
        return list_collection[0]

    merged = [
        merge(list_collection[i], list_collection[i + 1])
        for i in range(0, len(list_collection) - 1, 2)
    ]

    if len(list_collection) % 2 != 0:
        merged.append(list_collection[-1])

    return merge_n_list(merged)

print(*merge_n_list(full_list))
