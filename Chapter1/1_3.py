def URLify(string, num):
    string = list(string)
    countSpace = 0
    for i in range(num) :
        if string[i] == ' ': countSpace += 1
    countSpace *= 2
    realLength = num + countSpace - 1
    
    for i in range(num - 1, -1, -1) :
        if string[i] == ' ':
            string[realLength] = '0'
            string[realLength - 1] = '2'
            string[realLength - 2] = '%'
            realLength -= 3
        else:
            string[realLength] = string[i]
            realLength -= 1
    
    return ''.join(string) # Convert list back to string


if __name__ == "__main__":
    string = "Mr John Smith    "
    num = 13

    print("Output: " + URLify(string, num))

