def max_product_of_three(n, numbers):

    max1, max2, max3 = sorted(numbers[:3], reverse=True)

    min1, min2, min3 = sorted(numbers[:3])

    for i in range(3, n):

        if numbers[i] > max1:
            max1, max2, max3 = numbers[i], max1, max2

        elif numbers[i] > max2:
            max2, max3 = numbers[i], max2

        elif numbers[i] > max3:
            max3 = numbers[i]

        if numbers[i] < min1:
            min1, min2, min3 = numbers[i], min1, min2

        elif numbers[i] < min2:
            min2, min3 = numbers[i], min2

        elif numbers[i] < min3:
            min3 = numbers[i]

    return max(max1 * max2 * max3, min1 * min2 * max1)


if __name__ == '__main__':

    n = int(input())
    numbers = [int(i) for i in input().split()]
    print(max_product_of_three(n, numbers))
