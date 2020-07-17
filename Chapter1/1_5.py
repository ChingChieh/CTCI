def checkOneEdit(string1, string2):
    # User can perform 1.insert 2.remove 3.replace
    len_diff = abs(len(string1) - len(string2))
    if len_diff > 1:
        return False
    elif len_diff == 0:
        diff = False
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                if diff:
                    return False
                diff = True

    else:
        # longString = string1 if len(string1) > len(string2) else string2
        # shortString = string1 if len(string1) < len(string2) else string2
        if len(string1) > len(string2):
            longString, shortString = string1, string2
        else:
            longString, shortString = string2, string1
        shift = 0
        for i in range(len(shortString)):
            if longString[i + shift] != shortString[i]:
                if shift:
                    return False
                shift = 1
    return True

if __name__ == "__main__":
    import sys
    print(checkOneEdit(sys.argv[1], sys.argv[2]))
