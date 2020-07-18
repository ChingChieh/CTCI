import sys
def stringCompress(string):
    stringLen = len(string)
    count = 1
    string = string + '\0'
    part = []
    for i in range(stringLen):
        if string[i] == string[i + 1]:
            count += 1
        else:
            part.append(string[i] + str(count))
            count = 1
    result = "".join(part)
    if len(result) > stringLen:
        return string
    else:
        return result
if __name__ == "__main__":
    print(stringCompress(sys.argv[-1]))
