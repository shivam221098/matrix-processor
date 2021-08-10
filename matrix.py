def operation_matrix(operator):
    print("Enter first matrix: ")
    matrix_a, row_a, col_a = create_matrix()
    print("Enter socond matrix: ")
    matrix_b, row_b, col_b = create_matrix()
    result = []
    if row_a == row_b and col_a == col_b:
        for i, j in zip(matrix_a, matrix_b):
            temp = []
            for k, l in zip(i, j):
                if operator == "+":
                    temp.append(k + l)
                elif operator == "-":
                    temp.append(k - l)
            result.append(temp)
    return result


def create_matrix():
    row, col = map(int, input("Enter rows & columns: ").split())
    matrix = []
    for i in range(row):
        temp = list(map(int, input().split()))
        if len(temp) == col:
            matrix.append(temp)
        else:
            print("Invalid matrix")
            break
    return matrix, row, col


if __name__ == '__main__':
    # print(create_matrix())
    print(operation_matrix("-"))