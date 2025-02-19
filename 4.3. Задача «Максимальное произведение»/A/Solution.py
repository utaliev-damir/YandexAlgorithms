def max_pairwise(numbers, n):

    first_idx = 0

    for i in range(1, n):
        if numbers[i] > numbers[first_idx]:
            first_idx = i

    second_idx = 0 if first_idx != 0 else 1

    for i in range(second_idx + 1, n):
        if numbers[i] > numbers[second_idx] and i != first_idx:
            second_idx = i

    return numbers[first_idx] * numbers[second_idx]


if __name__ == '__main__':

    n = int(input())
    numbers = [int(i) for i in input().split()]
    print(max_pairwise(numbers, n))
