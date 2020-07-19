def isSubstring(s1, s2):
    return (s1 in s2)


def isRotate(s1, s2):
    s1Len = len(s1)
    if (s1Len == len(s2) and s1Len > 0):
        s2 = "".join([s2,s2])
        return isSubstring(s1, s2)
    return False

if __name__ == "__main__":
    import sys
    print(isRotate(sys.argv[-2], sys.argv[-1]))
