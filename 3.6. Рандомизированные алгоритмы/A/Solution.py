n = int(input())

lst = list(map(int, input().split()))


def lomuto_partition(lst):
    border = lst[0]

    i = 1
    pointer = 1

    while i < len(lst):

        if lst[i] < border:
            lst[pointer], lst[i] = lst[i], lst[pointer]
            pointer += 1
        i += 1
    lst[0], lst[pointer - 1] = lst[pointer - 1], lst[0]
    return lst


print(*lomuto_partition(lst))
