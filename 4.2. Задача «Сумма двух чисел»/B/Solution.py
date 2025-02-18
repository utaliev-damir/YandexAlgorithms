def polynomial_sum(poly1, poly2):
    
    long_poly, short_poly = (poly1, poly2) if len(poly1) > len(poly2) else (poly2, poly1)
    
    short_poly = [0] * (len(long_poly) - len(short_poly)) + short_poly

    return len(long_poly) - 1, [a + b for a, b in zip(long_poly, short_poly)]


if __name__ == '__main__':
    n1 = int(input())
    poly1 = list(map(int, input().split()))
    n2 = int(input())
    poly2 = list(map(int, input().split()))
    degree, poly_sum = polynomial_sum(poly1, poly2)
    print(degree)
    print(*poly_sum)
