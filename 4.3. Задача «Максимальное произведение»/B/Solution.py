def is_comparison_count_above_threshold(n, threshold):

    if 1 + 2 * (n - 2) > threshold * n:
        case = list(range(n))
        case[-1], case[0] = case[0], case[-1]
        return 'YES', case
    return 'NO', []


if __name__ == '__main__':

    n = int(input())
    result, case = is_comparison_count_above_threshold(n, 1.5)
    print(result)
    if case:
        print(*case)
