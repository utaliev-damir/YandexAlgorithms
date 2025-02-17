import random

n = int(input())

lst = list(map(int, input().split()))


def lomuto_partition(lst, low, high):

    pivot_index = random.randint(low, high)
    lst[low], lst[pivot_index] = lst[pivot_index], lst[low]

    border = lst[low]
    pointer = low + 1

    for j in range(low + 1, high + 1):
        if lst[j] < border:
            lst[pointer], lst[j] = lst[j], lst[pointer]
            pointer += 1

    lst[low], lst[pointer - 1] = lst[pointer - 1], lst[low]
    return pointer - 1


def quick_sort(lst, low=0, high=None):

    if high is None:
        high = len(lst) - 1

    if low < high:
        pointer_idx = lomuto_partition(lst, low, high)
        quick_sort(lst, low, pointer_idx)
        quick_sort(lst, pointer_idx + 1, high)

    return lst


print(*quick_sort(lst))
