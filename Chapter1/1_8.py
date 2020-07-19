def printMatrix(array):
    length = len(array)
    for i in range(length):
        print(array[i])
    print("")
def nullifyRow(matrix, row, col):
    for i in range(col):
        matrix[row][i] = 0
def nullifyCol(matrix, row, col):
    for i in range(row):
        matrix[i][col] = 0

def setZero(matrix):
    # time complexity: O(N^2)
    # Use the first column and first row to store zero index
    row = len(matrix)
    col = len(matrix[0])
    rowHasZero = False
    colHasZero = False
    for i in range(col):
        if matrix[0][i] == 0:
            rowHasZero = True
            break
    for j in range(row):
        if matrix[j][0] == 0:
            colHasZero = True
            break

    for i in range(1, row):
        for j in range(1, col):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, row):
        if matrix[i][0] == 0:
            nullifyRow(matrix, i, col)
    for i in range(1, col):
        if matrix[0][i] == 0:
            nullifyCol(matrix, row, i)
    if rowHasZero:
        nullifyRow(matrix, 0, col)
    if colHasZero:
        nullifyCol(matrix, row, 0)
if __name__ == "__main__":
    matrix = [
    [0, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2],
    [3, 3, 0, 3, 3, 3],
    [4, 4, 4, 4, 4, 4],
    [5, 5, 5, 5, 0, 5],
    [6, 6, 6, 6, 6, 6]]
    printMatrix(matrix)
    setZero(matrix)
    printMatrix(matrix)
