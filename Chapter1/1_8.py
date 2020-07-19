def printMatrix(array):
    length = len(array)
    for i in range(length):
        print(array[i])
    print("")
def setZero(matrix):
    # Use the first row we spot that contain zero as buffer
    counter = -1
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                if counter < 0:
                    counter = i
                matrix[counter][j] = 0

    for i in range(row):
        for j in range(col):
            if i == counter:
                break;
            if matrix[i][j] == 0:
                matrix[i] = [0] * row
                break;

    if counter != -1:
        for l in range(col):
            if matrix[counter][l] == 0:
                for m in range(row):
                    matrix[m][l] = 0
        matrix[counter] = [0] * col

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
