def CheckPermutation(string1, string2):
    if len(string1) != len(string2) : return False
    charSet = [0] * 128 # Using the hashtable
    for i in string1:
        charSet[ord(i)] += 1
    
    for i in string2:
        charSet[ord(i)] -= 1
        if charSet[ord(i)] < 0:
            return False

    return True

def Check(string1, string2):

    if len(string1) != len(string2) : return False
    list(string1).sort()
    list(string2).sort()
    for i,j in zip(string1, string2):  # remember to use zip!!!
        if i != j : return False
    return True


if __name__ == "__main__" :
    string1 = "abcdefghijk"
    string2 = "abcdfeijkhk"
    print("Is string2 is a permutation of string1 : " + str(CheckPermutation(string1, string2)))
    print("Is string2 is a permutation of string1 : " + str(Check(string1, string2)))
