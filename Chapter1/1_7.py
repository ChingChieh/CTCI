import sys

def printMatrix(array):
    length = len(array)
    for i in range(length):
        print(array[i])
    print("")
def rotateMatrix(array):
    row = len(array)
    head = 0
    tail = row - 1
    for t in range(row / 2):
        do = row - (t * 2) - 1
        for i in range(do):
            tmp1 = array[i + head][tail]
            array[i + head][tail] = array[head][i + head]
            tmp2 = array[tail][tail - i]
            array[tail][tail - i] = tmp1
            tmp1 = array[tail - i][head]
            array[tail - i][head] = tmp2
            array[head][i + head] = tmp1
        head = head + 1
        tail = tail - 1


if __name__ == "__main__":
    array = [
    [1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5, 5],
    [6, 6, 6, 6, 6, 6]]

    printMatrix(array)

    rotateMatrix(array)

    printMatrix(array)
