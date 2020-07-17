class solution:
    def isUniqueChars(self, string):
        if len(string) > 128 : return False

        char_set = [False] * 128
        for i in range(len(string)) :
            val = ord(string[i])
            if (char_set[val]) : return False
            char_set[val] = True
        
        return True
    

if __name__ == "__main__":
    answer = solution()
    string = "abcdefghijka"
    print(answer.isUniqueChars(string))
