def checkOneEdit(string1, string2):
    # User can perform 1.insert 2.remove 3.replace
    if abs(len(string1) - len(string2)) > 1:
        return False
    if string1 == string2:
        return True
    longString = string1 if len(string1) > len(string2) else string2
    shortString = string1 if len(string1) < len(string2) else string2
    count = 0;
    if len(longString) == len(shortString):
        for i in range(len(longString)):
            if longString[i] != shortString[i]:
                count += 1
                if count > 1:
                    return False
    else:
        diff = 0
        for i in range(len(shortString)):
            if longString[i + diff] != shortString[i]:
                if diff == 1:
                    return False
                diff = 1


    return True

if __name__ == "__main__":
    import sys
    print(checkOneEdit(sys.argv[1], sys.argv[2]))
