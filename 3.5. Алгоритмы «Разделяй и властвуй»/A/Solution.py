n = int(input())
lst = [int(k) for k in input().split()]

def select_sort(lst):
    n = len(lst)

    for i in range(n):

        min_index = i
        for k in range(i, n):
            if lst[k] < lst[min_index]:
                min_index = k
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

print(*select_sort(lst))
