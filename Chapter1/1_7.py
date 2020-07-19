import sys

def printArray(array):
    length = len(array)
    for i in range(length):
        print(array[i])
    print("")
def rotateArray90(array):
    row = len(array)
    head = 0
    tail = row - 1
    tmp1 = []
    tmp2 = []
    tmp3 = []
    for t in range(row / 2):
        do = row - (t * 2) - 1
        for i in range(do):
            tmp1.append(array[i + head][tail])
            array[i + head][tail] = array[head][i + head]
            tmp2.append(array[tail][tail - i])
            array[tail][tail - i] = tmp1[i]
            tmp3.append(array[tail - i][head])
            array[tail - i][head] = tmp2[i]
            array[head][i + head] = tmp3[i]
        head = head + 1
        tail = tail - 1
        tmp1 = []
        tmp2 = []
        tmp3 = []


if __name__ == "__main__":
    array = [
    [1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5, 5],
    [6, 6, 6, 6, 6, 6]]

    printArray(array)

    rotateArray90(array)

    printArray(array)
