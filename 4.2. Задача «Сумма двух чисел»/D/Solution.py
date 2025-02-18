def sum_matrix(n, m, matrix1, matrix2):

    result = []

    for i in range(n):
        row = []
        for j in range(m):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

def print_matrix(matrix):

    for row in matrix:
        print(' '.join(map(str, row)))


if __name__ == '__main__':

    n, m = (int(i) for i in input().split())

    matrix1 = [list(map(int, input().split())) for _ in range(n)]
    matrix2 = [list(map(int, input().split())) for _ in range(n)]

    result = sum_matrix(n, m, matrix1, matrix2)
    print_matrix(result)
