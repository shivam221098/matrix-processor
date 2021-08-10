from matrix import create_matrix


def const_mul():
    print("Enter matrix: ")
    matrix, row, col = create_matrix()
    const = input("Enter constant number")
    print(matrix, const)


const_mul()