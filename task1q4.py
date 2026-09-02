def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0]) if rows_a > 0 else 0
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0]) if rows_b > 0 else 0

    if cols_a != rows_b or cols_a == 0:
        print(f"Error: Cannot multiply matrices. Inner dimensions do not match.")
        print(f"Matrix A columns ({cols_a}) != Matrix B rows ({rows_b}).")
        return None

    result = [[0 for j in range(cols_b)] for i in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result

input_A = input('enter matix A: ')
A = [list(map(int,r.split()))for r in input_A.split(',')] #separate rows with comma and numbers with space


input_B = input('enter matix B: ')
B = [list(map(int,r.split()))for r in input_B.split(',')] #separate rows with comma and numbers with space

print(multiply_matrices(A, B))
